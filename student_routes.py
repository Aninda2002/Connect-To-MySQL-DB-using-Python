from flask import Blueprint, request, jsonify
from models.db import get_connection

student_bp = Blueprint("student_bp", __name__)

@student_bp.route("/students", methods=["POST"])
def create_student():
    data = request.get_json()

    conn = get_connection()
    cursor = conn.cursor()

    query = "INSERT INTO students (name, age) VALUES (%s, %s)"
    cursor.execute(query, (data["name"], data["age"]))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Student created"}), 201


@student_bp.route("/students", methods=["GET"])
def get_students():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students")
    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return jsonify(result)


@student_bp.route("/students/<int:id>", methods=["GET"])
def get_student(id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM students WHERE id=%s", (id,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return jsonify(result)


@student_bp.route("/students/<int:id>", methods=["PUT"])
def update_student(id):
    data = request.get_json()

    conn = get_connection()
    cursor = conn.cursor()

    query = "UPDATE students SET name=%s, age=%s WHERE id=%s"
    cursor.execute(query, (data["name"], data["age"], id))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Student updated"})



@student_bp.route("/students/<int:id>", methods=["DELETE"])
def delete_student(id):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("DELETE FROM students WHERE id=%s", (id,))
    conn.commit()

    cursor.close()
    conn.close()

    return jsonify({"message": "Student deleted"})
