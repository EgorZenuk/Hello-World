from flask import *
from classes.data import info
from methods.simplex import simplex_method
from methods.evolution import get_answer

application = Flask(__name__)


@application.route("/", methods=["POST", "GET"])
def menu():
    if request.method == "POST":
        oper1_time1 = float(request.form.get("processing_time-1A"))
        oper1_time2 = float(request.form.get("processing_time-1B"))
        oper1_time3 = float(request.form.get("processing_time-1C"))
        operation_times_1 = [oper1_time1, oper1_time2, oper1_time3]

        oper2_time1 = float(request.form.get("processing_time-2A"))
        oper2_time2 = float(request.form.get("processing_time-2B"))
        oper2_time3 = float(request.form.get("processing_time-2C"))
        operation_times_2 = [oper2_time1, oper2_time2, oper2_time3]

        price1 = float(request.form.get("price_A"))
        price2 = float(request.form.get("price_B"))
        price3 = float(request.form.get("price_C"))
        prices = [price1, price2, price3]

        work_time = float(request.form.get("work_time"))
        number_rele = float(request.form.get("number_rele"))

        info.data["operation_times_1"] = operation_times_1
        info.data["operation_times_2"] = operation_times_2
        info.data["prices"] = prices
        info.data["work_time"] = work_time
        info.data["number_rele"] = number_rele

        print(info.data)
    return render_template("main.html")


@application.route("/simplex", methods=["POST", "GET"])
def simplex_page():
    value, variable = simplex_method(info.data)
    return render_template("simplex.html", value=value, variable=variable)


@application.route("/evolution", methods=["POST", "GET"])
def evolution_page():
    variable, value = get_answer(info.data)
    return render_template("evolution.html", value=value, variable=variable)


@application.route("/download", methods=["POST", "GET"])
def solves_page():
    return send_file("internal_solve/solves.txt")


@application.route("/under_task", methods=["POST", "GET"])
def under_task():
    return render_template("under_task.html")


if __name__ == "__main__":
    application.run(debug=True)
