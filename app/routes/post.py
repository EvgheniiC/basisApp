from flask import Blueprint, render_template, request, redirect, flash, abort
from flask_login import login_required, current_user

from ..forms import StudentForm, TeacherForm
from ..extensions import db
from ..models.post import Post
from ..models.user import User

post = Blueprint("post", __name__)


@post.route("/", methods=["POST", "GET"])
def all():
    # sort all posts order_by(Post.date)
    form = TeacherForm()
    form.teacher.choices = [teacher.name for teacher in User.query.filter_by(status = "teacher")]
    if request.method == "POST":
        teacher = request.form.get("teacher")
        teacher_id = User.query.filter_by(name=teacher).first().id
        posts = Post.query.filter_by(teacher=teacher_id).order_by(Post.date.desc()).all()
    else:
        posts = Post.query.order_by(Post.date.desc()).limit(20).all()


    return render_template("post/all.html", posts=posts, user=User, form=form)


@post.route("/post/create", methods=["POST", "GET"])
@login_required
def create():
    form = StudentForm()
    form.student.choices = [student.name for student in User.query.filter_by(status = "user")]
    if request.method == "POST":
        student = request.form.get("student")
        subject = request.form.get("subject")
        student_id = User.query.filter_by(name = student).first().id

        post = Post(teacher=current_user.id, student=student_id, subject=subject)
        flash(f"Successful posted!", "success")
        try:
            db.session.add(post)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print(e)
    else:
        return render_template("post/create.html",form=form)


@post.route("/post/<int:id>/update", methods=["POST", "GET"])
@login_required
def update(id: int):
    post = Post.query.get(id)
    if post.author.id == current_user.id:
        form = StudentForm()
        form.student.data = User.query.filter_by(id = post.student).first().name
        form.student.choices = [student.name for student in User.query.filter_by(status = "user")]
        if request.method == "POST":
            student = request.form.get("student")
            post.subject = request.form.get("subject")

            post.student_id = User.query.filter_by(name=student).first().id
            try:
                db.session.commit()
                flash(f"Successful updated!", "update")
                return redirect("/")
            except Exception as e:
                print(e)
        else:
            return render_template("post/update.html", post=post, form=form)
    else:
        abort(403)

@post.route("/post/<int:id>/delete", methods=["DELETE", "GET"])
@login_required
def delete(id: int):
    post = Post.query.get(id)
    if post.author.id == current_user.id:
        try:
            db.session.delete(post)
            db.session.commit()
            flash(f"Successful deleted!", "success")
            return redirect("/")
        except Exception as e:
            print(e)
    else:
        abort(403)

