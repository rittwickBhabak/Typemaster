# app.py
from myproject import app, db
from flask import Flask, render_template, redirect, flash, url_for, request, abort
from flask_login import login_user, login_required, logout_user
# from myproject.models import User, PracticeLine, Exercise
# from myproject.forms import LoginForm, RegistrationForm

