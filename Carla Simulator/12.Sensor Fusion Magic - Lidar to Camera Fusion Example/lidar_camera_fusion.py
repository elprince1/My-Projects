#!/usr/bin/env python

# Copyright (c) 2020 Computer Vision Center (CVC) at the Universitat Autonoma de
# Barcelona (UAB).
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.

"""
Lidar projection on RGB camera example
"""
import time
import glob
import os
import sys

try:
    sys.path.append(glob.glob('../carla/dist/carla-*%d.%d-%s.egg' % (
        sys.version_info.major,
        sys.version_info.minor,
        'win-amd64' if os.name == 'nt' else 'linux-x86_64'))[0])
except IndexError:
    pass

import carla

import argparse
from queue import Queue
from queue import Empty
from matplotlib import cm
from PIL import ImageDraw
from PIL import ImageFont
from ultralytics import YOLO

try:
    import numpy as np
except ImportError:
    raise RuntimeError('cannot import numpy, make sure numpy package is installed')

try:
    from PIL import Image
except ImportError:
    raise RuntimeError('cannot import PIL, make sure "Pillow" package is installed')

VIRIDIS = np.array(cm.get_cmap('viridis').colors)
VID_RANGE = np.linspace(0.0, 1.0, VIRIDIS.shape[0])

os.environ['KMP_DUPLICATE_LIB_OK']='True'


def BBoxDistance(model,results,points_2d,test_img,num,points_2d_without_normalize):
    List_Objects=[]
    
    list_bboxes=list(results[0].boxes.xywh)
    list_labels=list(results[0].boxes.cls)
    
    #im_array = np.array(Image.open('img.jpg').convert("RGB"))
    # results[0].save('img.jpg')
    # img=Image.open('img.jpg').convert("RGB")
    # test_img=np.array(img)
   
    count=0
    for bbox in list_bboxes:
        
        label=model.names[int(list_labels[count])]
        # bbox=[x,y,width,height]
        
        x1=int(bbox[0])-int(bbox[2])/2
        y1=int(bbox[1])-int(bbox[3])/2
        
        
        x2=int(bbox[0])+int(bbox[2])/2
        y2=int(bbox[1])+int(bbox[3])/2
        
        points_mask = \
                (points_2d[:, 0] > x1) & (points_2d[:, 0] < x2) & \
                (points_2d[:, 1] > y1) & (points_2d[:, 1] < y2)
                
        points_2d_mod = points_2d[points_mask]
        points_2d_without_normalize_mod = points_2d_without_normalize[points_mask]
        
        u_coord=points_2d_mod[:,0].astype(int)
        v_coord=points_2d_mod[:,1].astype(int)
        
        
        for i in range(len(points_2d_mod)):
            # I'm not a NumPy expert and I don't know how to set bigger dots
            # without using this loop, so if anyone has a better solution,
            # make sure to update this script. Meanwhile, it's fast enough :)
            test_img[
                v_coord[i],
                u_coord[i]] = 255

        #print(points_2d_mod[:,0])
        


        #print(points_2d_mod[:,2])
        if len(points_2d_mod)!=0: ## x distance, y distance
            List_Objects.append({label: [np.min(points_2d_mod[:,2].astype(int)),np.min((abs(points_2d_without_normalize_mod[:,0])).astype(int))]})
        count+=1
    
    #print(List_Objects)
    #imgFarray = Image.fromarray(test_img)
    #imgFarray.save(f"_out\\{num}.png")
    

    return List_Objects,test_img



  
    
def hot_one_coding(list_obj_dist):
    list_hot_one=[0]*8 #[red-green-yellow-red-green-yellow]
    for ele in list_obj_dist:
        if list(ele.keys())[0]=="red" or list(ele.keys())[0]=="yellow":
            list_hot_one[0] = 1
            if list(ele.values())[0][0] < list_hot_one[4] or list_hot_one[4]==0:
                list_hot_one[4] = list(ele.values())[0][0]/100
        elif list(ele.keys())[0]=="green":
            list_hot_one[1] = 1
            if list(ele.values())[0][0] < list_hot_one[5] or list_hot_one[5]==0:
                list_hot_one[5] = list(ele.values())[0][0]/100
        elif list(ele.keys())[0]=="car" or list(ele.keys())[0]=="motorcycle" or list(ele.keys())[0]=="bus" or \
             list(ele.keys())[0]=="truck" or list(ele.keys())[0]=="person":
            
            if list(ele.values())[0][1]<1:
                list_hot_one[2] = 1
                if((list(ele.values())[0][0] < list_hot_one[6]) or list_hot_one[6]==0):
                    list_hot_one[6] = list(ele.values())[0][0]/100
            else:
                list_hot_one[3] = 1
                if((list(ele.values())[0][0] < list_hot_one[7]) or list_hot_one[7]==0):
                    list_hot_one[7] = list(ele.values())[0][0]/100
            
                
    return np.array(list_hot_one)
    

def FusionLidarCamera(image_data,lidar_data,lidar,camera,image_w,image_h):

    #model = YOLO("data.yaml")
    model1 = YOLO("best.pt")
    model2 = YOLO("yolov8n.pt")

    # Build the K projection matrix:
        # K = [[Fx,  0, image_w/2],
        #      [ 0, Fy, image_h/2],
        #      [ 0,  0,         1]]
        
    fov = 90.0
    focal = image_w / (2.0 * np.tan(fov * np.pi / 360.0))

    # In this case Fx and Fy are the same since the pixel aspect
    # ratio is 1
    K = np.identity(3)
    K[0, 0] = K[1, 1] = focal
    K[0, 2] = image_w / 2.0
    K[1, 2] = image_h / 2.0


    # Get the raw BGRA buffer and convert it to an array of RGB of
    # shape (image_data.height, image_data.width, 3).
    im_array = np.copy(np.frombuffer(image_data.raw_data, dtype=np.dtype("uint8")))
    im_array = np.reshape(im_array, (image_data.height, image_data.width, 4))
    im_array = im_array[:, :, :3][:, :, ::-1]
    

    # Get the lidar data and convert it to a numpy array.
    p_cloud_size = len(lidar_data)
    p_cloud = np.copy(np.frombuffer(lidar_data.raw_data, dtype=np.dtype('f4')))
    p_cloud = np.reshape(p_cloud, (p_cloud_size, 4))

    # Lidar intensity array of shape (p_cloud_size,) but, for now, let's
    # focus on the 3D points.
    intensity = np.array(p_cloud[:, 3])

    # Point cloud in lidar sensor space array of shape (3, p_cloud_size).
    local_lidar_points = np.array(p_cloud[:, :3]).T

    # Add an extra 1.0 at the end of each 3d point so it becomes of
    # shape (4, p_cloud_size) and it can be multiplied by a (4, 4) matrix.
    local_lidar_points = np.r_[
        local_lidar_points, [np.ones(local_lidar_points.shape[1])]]

    # This (4, 4) matrix transforms the points from lidar space to world space.
    lidar_2_world = lidar.get_transform().get_matrix()

    # Transform the points from lidar space to world space.
    world_points = np.dot(lidar_2_world, local_lidar_points)

    # This (4, 4) matrix transforms the points from world to sensor coordinates.
    world_2_camera = np.array(camera.get_transform().get_inverse_matrix())

    # Transform the points from world space to camera space.
    
    sensor_points = np.dot(world_2_camera, world_points)

    

    # New we must change from UE4's coordinate system to an "standard"
    # camera coordinate system (the same used by OpenCV):

    # ^ z                       . z
    # |                        /
    # |              to:      +-------> x
    # | . x                   |
    # |/                      |
    # +-------> y             v y

    # This can be achieved by multiplying by the following matrix:
    # [[ 0,  1,  0 ],
    #  [ 0,  0, -1 ],
    #  [ 1,  0,  0 ]]

    # Or, in this case, is the same as swapping:
    # (x, y ,z) -> (y, -z, x)
    point_in_camera_coords = np.array([
        sensor_points[1],
        sensor_points[2] * -1,
        sensor_points[0]])

    points_2d_without_normalize = point_in_camera_coords
    # Finally we can use our K matrix to do the actual 3D -> 2D.
    points_2d = np.dot(K, point_in_camera_coords)


    # Remember to normalize the x, y values by the 3rd value.
    # points_2d_without_normalize = np.array([
    #     points_2d[0, :],
    #     points_2d[1, :],
    #     points_2d[2, :]])

    points_2d = np.array([
        points_2d[0, :] / points_2d[2, :],
        points_2d[1, :] / points_2d[2, :],
        points_2d[2, :]])

    

    # At this point, points_2d[0, :] contains all the x and points_2d[1, :]
    # contains all the y values of our points. In order to properly
    # visualize everything on a screen, the points that are out of the screen
    # must be discarted, the same with points behind the camera projection plane.
    points_2d = points_2d.T
    points_2d_without_normalize = points_2d_without_normalize.T
    intensity = intensity.T
    points_in_canvas_mask = \
        (points_2d[:, 0] > 0.0) & (points_2d[:, 0] < image_w) & \
        (points_2d[:, 1] > 0.0) & (points_2d[:, 1] < image_h) & \
        (points_2d[:, 2] > 0.0)
    points_2d = points_2d[points_in_canvas_mask]
    points_2d_without_normalize = points_2d_without_normalize[points_in_canvas_mask]
    intensity = intensity[points_in_canvas_mask]
    
        
    
    # Extract the screen coords (uv) as integers.
    u_coord = points_2d[:, 0].astype(int)
    v_coord = points_2d[:, 1].astype(int)

    # Since at the time of the creation of this script, the intensity function
    # is returning high values, these are adjusted to be nicely visualized.
    intensity = 4 * intensity - 3
    color_map = np.array([
        np.interp(intensity, VID_RANGE, VIRIDIS[:, 0]) * 255.0,
        np.interp(intensity, VID_RANGE, VIRIDIS[:, 1]) * 255.0,
        np.interp(intensity, VID_RANGE, VIRIDIS[:, 2]) * 255.0]).astype(int).T
    
    results1 = model1(im_array,imgsz=(1280,736))
    im_array = results1[0].plot()

    print(im_array.shape)
    results2 = model2(im_array,conf=0.5,imgsz=(1280,736))
    im_array = results2[0].plot()

    print(im_array.shape)

    if 1 <= 0:
        # Draw the 2d points on the image as a single pixel using numpy.
        im_array[v_coord, u_coord] = color_map
        #pass
    else:
        # Draw the 2d points on the image as squares of extent args.dot_extent.
        for i in range(len(points_2d)):
            # I'm not a NumPy expert and I don't know how to set bigger dots
            # without using this loop, so if anyone has a better solution,
            # make sure to update this script. Meanwhile, it's fast enough :)
            im_array[
                v_coord[i]-1 : v_coord[i]+1,
                u_coord[i]-1 : u_coord[i]+1] = color_map[i]
        #pass
    
    ## temp
    

    dist,im_array=BBoxDistance(model1,results1,points_2d,im_array,image_data.frame,points_2d_without_normalize)
    dist2,im_array=BBoxDistance(model2,results2,points_2d,im_array,image_data.frame,points_2d_without_normalize)

    dist.extend(dist2)

    #Save the image using Pillow module.
    #image = Image.fromarray(im_array)
    
    # I1 = ImageDraw.Draw(image)
    
    # cnt=0
    # for value in dist:
        
    #     #print(value)
    #     I1.text((10, cnt+36), f"{list(value.keys())[0]}: {list(value.values())[0]}m", fill="Orange",font=ImageFont.truetype('arial', 20))
        
    #     cnt+=20
    
    #image.save("_out/%08d.png" % image_data.frame)
    # image = Image.fromarray(im_array)
    # image.save("_out/%08d.png" % image_data.frame)
    # print(np.min(points_2d[:,2].astype(int)))
    res=hot_one_coding(dist)
    return res,im_array
    
