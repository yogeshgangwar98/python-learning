class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector{self.x, self.y}"
    
    def __add__(self, obj):
        return Vector(self.x+obj.x, self.y+obj.y)
    
v1 = Vector(3,4)
v2 = Vector(5,2)
v3 = v1+v2
print(v3)

print(v1)