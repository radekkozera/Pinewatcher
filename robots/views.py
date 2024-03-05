from django.shortcuts import render
from django.http import JsonResponse
from .models import Robot

def get_all_robots(request):
    robots = Robot.objects.all()
    robot_list = [{'serial_number': robot.serial_number, 'type': robot.type} for robot in robots]
    return JsonResponse(robot_list, safe=False)
