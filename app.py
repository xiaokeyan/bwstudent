from flask import Flask,render_template,request,redirect,url_for
from dbs import db
import config
from models import Student,Performance
app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
@app.route('/',methods=["post","get"])
def index():
    # db.create_all()
    a = Student.query.all()
    id = request.args.get("id")
    sort = request.args.get("sort")
    if request.method == "POST":
        search = request.form.get("search")
        if search:
            search1 = Student.query.filter(Student.name.like("%"+search+"%")).all()
            return render_template("index.html",a = search1)
    if sort == "1":
        w = Performance.query.order_by(Performance.total_score).all()
        return render_template("index.html",w = w)
    elif sort == "2":
        w = Performance.query.order_by(Performance.total_score.desc()).all()
        return render_template("index.html", w = w)
    else:
        pass
    if id:
        dat=Performance.query.filter_by(id=int(id)).first()
        dat1 = dat.g_cus.id
        dat2 = Student.query.filter_by(id=int(dat1)).first()
        db.session.delete(dat)
        db.session.delete(dat2)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("index.html",a = a)



@app.route('/add/',methods=['post','get'])
def add():
    if request.method == 'POST':
        name = request.form.get("name")
        python = request.form.get("python")
        big_data = request.form.get("big_data")
        h5 = request.form.get("h5")
        if name and python and big_data and h5:
            total_score = int(python)+int(big_data)+int(h5)
            dat1=Student(name=name)
            dat2=Performance(python=python,big_data=big_data,h5=h5,total_score=total_score)
            dat2.g_cus = dat1
            db.session.add(dat1)
            db.session.commit()
            return redirect(url_for('index'))
    return render_template("add.html")
@app.route('/alter/',methods=["post","get"])
def alter():
    if request.method == "POST":
        id = request.args.get("id")
        name1 = request.form.get("name1")
        python1 = request.form.get("python1")
        big_data1 = request.form.get("big_data1")
        h51 = request.form.get("h51")
        if name1 and python1 and big_data1 and h51:
            total_score1 = int(python1) + int(big_data1) + int(h51)
            Performance.query.filter_by(id=int(id)).update({"python":int(python1),"big_data":int(big_data1),"h5":int(h51),"total_score":total_score1})
            aa = Performance.query.filter_by(id=int(id)).first()
            bb = aa.g_cus.id
            Student.query.filter_by(id=int(bb)).update({"name":name1})
            db.session.commit()
            return redirect(url_for('index'))
    return render_template("alter.html")


if __name__ == '__main__':
    app.run()
