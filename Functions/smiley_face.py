"""
A program that draws a smiley face in turtle by using functions for an eye, the nose, and the mouth.
    The students should create functions that take parameters to create an eye, the nose, and the mouth.
    Make sure to emphasis that their preconditions and postconditions should match (e.g. if a function starts with the pen down, it should end with the pen down).
    The students should then create a function called draw_face that calls all of the previous functions and creates the face.
        You may wish to give them some of the proportions for time's sake.
    Make sure the students call turtle.done() in main after they're done drawing.

Created by Emma Lubes, eml5244, for the Academic Success Center Supplemental Instruction Program.
"""
import turtle

def draw_eye(radius, color):
    turtle.down()
    turtle.fillcolor("green")
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()

def draw_nose(side_length, color):
    turtle.down()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.forward(side_length)
    turtle.left(120)
    turtle.forward(side_length)
    turtle.left(120)
    turtle.forward(side_length)
    turtle.left(120)
    turtle.end_fill()
    turtle.up()

def draw_mouth(radius, smile_color, face_color):
    turtle.down()
    turtle.pencolor(smile_color)
    turtle.circle(radius)
    turtle.up()
    turtle.left(90)
    turtle.forward(radius*2.25)
    turtle.left(90)
    turtle.down()
    turtle.pencolor(face_color)
    turtle.fillcolor(face_color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.up()
    turtle.pencolor("black")
    turtle.left(90)
    turtle.forward(radius*2.25)
    turtle.left(90)

def draw_face(face_color, smile_color, eye_color, nose_color, nose_length, eye_radius, mouth_radius, face_radius):
    turtle.down()
    turtle.fillcolor(face_color)
    turtle.begin_fill()
    turtle.circle(face_radius)
    turtle.end_fill()
    turtle.up()
    turtle.left(90)
    turtle.forward(face_radius*1.25)
    turtle.right(90)
    turtle.backward(eye_radius*2)
    draw_eye(eye_radius, eye_color)
    turtle.forward(eye_radius*4)
    draw_eye(eye_radius, eye_color)
    turtle.backward(eye_radius*2)
    turtle.right(90)
    turtle.forward(nose_length*2)
    turtle.left(90)
    turtle.backward(nose_length*0.5)
    draw_nose(nose_length, nose_color)
    turtle.forward(nose_length*0.5)
    turtle.right(90)
    turtle.forward(face_radius*0.57)
    turtle.left(90)
    draw_mouth(mouth_radius, smile_color, face_color)
    turtle.right(90)
    turtle.forward(face_radius*0.18)
    turtle.left(90)

def main():
    turtle.speed(0)
    draw_face("yellow", "red", "green", "orange", 50, 25, 50, 200)
    turtle.done()

main()
