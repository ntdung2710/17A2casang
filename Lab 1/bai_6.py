import math

def add_vectors(a, b):
    return [a[0] + b[0], a[1] + b[1]]

def subtract_vectors(a, b):
    return [a[0] - b[0], a[1] - b[1]]

def vector_length(v):
    return math.sqrt(v[0] ** 2 + v[1] ** 2)

def dot_product(a, b):
    return a[0] * b[0] + a[1] * b[1]

def cosine_angle(a, b):
    dot = dot_product(a, b)
    length_a = vector_length(a)
    length_b = vector_length(b)
    if length_a == 0 or length_b == 0:
        return None  # Avoid division by zero
    return round(dot / (length_a * length_b), 2)

# Nhập tọa độ của hai vectơ a và b từ người dùng
a = [float(input("Nhập tọa độ x của vectơ a: ")), float(input("Nhập tọa độ y của vectơ a: "))]
b = [float(input("Nhập tọa độ x của vectơ b: ")), float(input("Nhập tọa độ y của vectơ b: "))]

# Phép cộng và phép trừ vectơ
sum_vector = add_vectors(a, b)
difference_vector = subtract_vectors(a, b)

# Độ dài của vectơ a và b
length_a = vector_length(a)
length_b = vector_length(b)

# Cosin góc giữa hai vectơ
cos_angle = cosine_angle(a, b)

# In kết quả
print("1. Phép cộng vectơ a + b:", sum_vector)
print("   Phép trừ vectơ a - b:", difference_vector)
print("2. Độ dài của vectơ a:", length_a)
print("   Độ dài của vectơ b:", length_b)
print("3. Cosin góc giữa hai vectơ a và b:", cos_angle)
