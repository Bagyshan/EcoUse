from pydantic import BaseModel
from flask import Flask, jsonify, request
from database import *
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy import func

app = Flask(__name__)


@app.route('/get_customer_warm/', methods=['GET'])
def get_customer_warm_rq():
    customer_warms = get_customer_warm()
    return jsonify({'data':customer_warms})

# @app.route('/get_avg_customer_warm/', methods=['GET'])
# def get_avg_customer_warm():
#     with SessionLocal() as db:
#         # Используем функцию func.avg() для вычисления среднего значения
#         average_rashod = db.query(func.avg(Customer_warm.rashod_na_kv_m)).scalar()

#     return jsonify({'average_rashod_na_kv_m': average_rashod})

@app.route('/create_customer_warm/', methods=['POST'])
def create_customer_warms():
    data = request.get_json()
    customer_warm = Customer_warmPydentic(
        rashod_na_kv_m=data.get('rashod_na_kv_m', 0)
    )
    create_customer_warm(customer_warm)

    return jsonify()
    
@app.route('/get_avg_customer_warm/', methods=['GET'])
def get_avg_customer_warm():
    avg_customer_warm = get_avg_rashod()
    return jsonify({'avarage_rashod_na_kv_m':avg_customer_warm})




@app.route('/get_customer_water/', methods=['GET'])
def get_customer_water_rq():
    customer_waters = get_customer_water()
    return jsonify({'data':customer_waters})


@app.route('/create_customer_water/', methods=['POST'])
def create_customer_waters():
    data = request.get_json()
    customer_water = Customer_water_Pydentic(
        rashod_na_cheloveka=data.get('rashod_na_cheloveka', 0)
    )
    create_customer_water(customer_water)

    return jsonify()

@app.route('/get_avg_customer_water/', methods=['GET'])
def get_avg_customer_water():
    avg_customer_water = get_avg_rashod_water()
    return jsonify({'avarage_rashod_na_cheloveka':avg_customer_water})






@app.route('/get_customer_svet/', methods=['GET'])
def get_customer_svet_rq():
    customer_svets = get_customer_svet()
    return jsonify({'data':customer_svets})


@app.route('/create_customer_svet/', methods=['POST'])
def create_customer_svets():
    data = request.get_json()
    customer_svet = Customer_svet_Pydentic(
        rashod_na_cheloveka=data.get('rashod_na_cheloveka', 0)
    )
    create_customer_svet(customer_svet)

    return jsonify()

@app.route('/get_avg_customer_svet/', methods=['GET'])
def get_avg_customer_svet():
    avg_customer_svet = get_avg_rashod_svet()
    return jsonify({'avarage_rashod_na_cheloveka':avg_customer_svet})





@app.route('/get_customer_gas/', methods=['GET'])
def get_customer_gas_rq():
    customer_gass = get_customer_gas()
    return jsonify({'data':customer_gass})


@app.route('/create_customer_gas/', methods=['POST'])
def create_customer_gass():
    data = request.get_json()
    customer_gas = Customer_gas_Pydentic(
        rashod_na_cheloveka=data.get('rashod_na_cheloveka', 0)
    )
    create_customer_gas(customer_gas)

    return jsonify()


@app.route('/get_avg_customer_gas/', methods=['GET'])
def get_avg_customer_gas():
    avg_customer_gas = get_avg_rashod_gas()
    return jsonify({'avarage_rashod_na_cheloveka':avg_customer_gas})










if __name__ == '__main__':
    try:
        app.run(host='localhost', port=8000)
    except Exception as e:
        print(f'An error occurred: {e}')
