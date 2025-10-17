import tkinter as tk

def draw_fractal(canvas, x, y, r, level, max_level):
    # Рисуем круг
    canvas.create_oval(x - r, y - r, x + r, y + r, outline="white")

    # Условие остановки
    if level >= max_level or r < 10:
        return

    # Радиус внутренних кругов
    new_r = r / 2.5

    # Координаты центров внутренних кругов (чуть ближе к центру)
    left_x = x - r / 2
    right_x = x + r / 2

    # Рисуем два меньших круга
    draw_fractal(canvas, left_x, y, new_r, level + 1, max_level)
    draw_fractal(canvas, right_x, y, new_r, level + 1, max_level)


def main():
    # Создаём окно
    root = tk.Tk()
    root.title("Фрактал — Рекурсия с кругами")

    # Холст
    canvas = tk.Canvas(root, width=800, height=800, bg="black")
    canvas.pack()

    # Рисуем фрактал (x, y, радиус, уровень, макс уровень)
    draw_fractal(canvas, 400, 400, 300, 0, 4)

    root.mainloop()


if __name__ == "__main__":
    main()
