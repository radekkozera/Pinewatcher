from django.shortcuts import render
from django.http import JsonResponse
from .models import Robot

def get_all_robots(request):
    robots = Robot.objects.all()
    robot_list = [{'type': robot.type, 'owner': robot.company} for robot in robots]
    return JsonResponse(robot_list, safe=False)
