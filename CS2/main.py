from pprint import pprint

from manim import *


class DefaultTemplate(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.flip(RIGHT)  # flip horizontally
        square.rotate(-3 * TAU / 8)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


class Variables(Scene):
    def construct(self):
        # Create screen halves
        LEFT_HALF = Rectangle(
            height=config.frame_height,
            width=config.frame_width / 2,
            stroke_width=0,
            fill_color=BLACK
        ).shift(LEFT * config.frame_width / 4)

        RIGHT_HALF = Rectangle(
            height=config.frame_height,
            width=config.frame_width / 2,
            stroke_width=0,
            fill_color=BLACK
        ).shift(RIGHT * config.frame_width / 4)

        # Add screen halves to scene
        self.add(LEFT_HALF, RIGHT_HALF)

        # Add vertical line
        halves_separator = Line(
            start=UP * config.frame_height / 2,
            end=DOWN * config.frame_height / 2,
            stroke_color=WHITE
        )

        self.play(Create(halves_separator))

        # DEBUG
        # guideline = DashedLine(
        #     start=UP * config.frame_height / 2,
        #     end=DOWN * config.frame_height / 2,
        #     stroke_color=WHITE
        # ).shift(config.frame_width / 4 * RIGHT)
        #
        # self.play(Create(guideline))

        # Add titles
        code_title = Text("Code")
        code_title.scale(0.75)
        code_title.move_to(LEFT_HALF.get_center()).to_edge(UP)

        self.play(Write(code_title))

        mem_title = Text("Memory")
        mem_title.scale(0.75)
        mem_title.move_to(RIGHT_HALF.get_center()).to_edge(UP)

        self.play(Write(mem_title))

        # Start writing code
        code = Code(
            "CS2/variables_code.txt",
        )
        code.move_to(LEFT_HALF.get_center())
        code.line_numbers.set_opacity(0.5)

        self.play(FadeIn(code.background), FadeIn(code.line_numbers))

        # First line
        x_var = Rectangle(height=1, width=1, fill_color=BLUE, fill_opacity=0.5).move_to(RIGHT_HALF.get_center())
        x_var_label = code.code_lines[0][0].copy()
        x_var_val_1 = VGroup(*code.code_lines[0][4:]).copy()

        x = VGroup(x_var, x_var_label, x_var_val_1)

        self.play(Write(code.code_lines[0]))

        self.wait(0.5)

        self.play(DrawBorderThenFill(x_var))
        self.play(x_var_label.animate.next_to(x_var, DOWN, buff=0.1))
        self.play(x_var_val_1.animate.move_to(x_var.get_center()))

        self.wait(2)

        # Second line
        y_var = (Rectangle(height=1, width=1, fill_color=BLUE, fill_opacity=0.5)
                 .next_to(x_var, RIGHT)
                 .shift(LEFT * (x.width / 2 + DEFAULT_MOBJECT_TO_MOBJECT_BUFFER / 2)))
        y_var_label = code.code_lines[1][0].copy()
        y_var_val_1 = VGroup(*code.code_lines[1][4:]).copy()

        y = VGroup(y_var, y_var_label, y_var_val_1)

        self.play(Write(code.code_lines[1]))

        self.wait(0.5)

        self.play(x.animate.shift(LEFT * (x.width / 2 + DEFAULT_MOBJECT_TO_MOBJECT_BUFFER / 2)))

        self.play(DrawBorderThenFill(y_var))
        self.play(y_var_label.animate.next_to(y_var, DOWN, buff=0.1))
        self.play(y_var_val_1.animate.move_to(y_var.get_center()))

        self.wait(2)

        # Third line
        self.play(Write(code.code_lines[2]))

        self.wait(0.5)

        self.play(Flash(code.code_lines[2][0]))
        self.play(Flash(x_var_label))

        self.wait(0.5)

        self.play(Flash(x_var_val_1, flash_radius=0.2))

        start = x_var_val_1.get_center()
        end = start + RIGHT * 3 + DOWN * 1.5
        control = start + UP * 3 + RIGHT * 1.5
        toss_path = CubicBezier(start, control, control, end)  # Smooth parabola

        arrow = Arrow(
            x_var_val_1.get_center() + RIGHT * 0.1 + UP * 0.1,
            x_var_val_1.get_center() + RIGHT + UP,
            buff=0.1
        )
        self.play(Create(arrow))

        self.play(
            MoveAlongPath(x_var_val_1, toss_path),
            FadeOut(arrow),
            run_time=1,
            rate_func=rate_functions.ease_in_cubic
        )

        self.remove(x_var_val_1)

        self.wait(1)

        x_var_val_2 = VGroup(*code.code_lines[2][4:]).copy()
        self.play(x_var_val_2.animate.move_to(x_var.get_center()))

        self.wait(2)
