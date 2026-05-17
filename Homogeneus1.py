%%manim -qm HomogeneousAnimation
# -*- coding: utf-8 -*-

from manim import *

class HomogeneousAnimation(Scene):
    def construct(self):
        # Color settings for clarity
        COLOR_LAMBDA = YELLOW
        COLOR_DEGREE = ORANGE
        COLOR_EQ = GREEN

        # ----------------------------------------------------------------
        # PART 1: Homogeneous Function Definition
        # ----------------------------------------------------------------
        title_1 = Text("Homogeneous Function of degree n", font_size=36, color=BLUE)
        title_1.to_edge(UP)
        self.play(Write(title_1))
        self.wait(0.5)

        # Base function
        func_base = MathTex("f(x, y)")
        func_base.move_to(UP * 1.5)
        self.play(FadeIn(func_base, shift=UP * 0.2))
        self.wait(0.5)

        # Function with lambda
        func_lambda = MathTex(
            "f(", "\\lambda", "x, ", "\\lambda", "y) =", 
            "\\lambda", "^n", "f(x, y)"
        )
        func_lambda.set_color_by_tex("\\lambda", COLOR_LAMBDA)
        func_lambda.set_color_by_tex("^n", COLOR_DEGREE)
        func_lambda.next_to(func_base, DOWN, buff=0.8)

        # Explanation text
        def_text1 = Tex(
            r"Arguments multiplied by $\lambda$ $\rightarrow$",
            font_size=40
        )
        def_text1.next_to(func_lambda, DOWN, buff=0.6)
        
        def_text2 = Tex(
            r"Result scales by $\lambda^n$",
            font_size=40
        )
        def_text2.next_to(def_text1, DOWN, buff=0.6)

        
        # Animation of formulas and text
        self.play(TransformMatchingShapes(func_base.copy(), func_lambda), run_time=2)
        self.play(Write(def_text1))
        self.play(Write(def_text2))
        self.wait(2.5)

        # Clear screen for part 2
        self.play(
            FadeOut(title_1),
            FadeOut(func_base),
            FadeOut(func_lambda),
            FadeOut(def_text1),
            FadeOut(def_text2)
        )
        self.wait(0.5)