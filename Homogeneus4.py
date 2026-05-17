%%manim -qm HomogeneousExample

from manim import *

class HomogeneousExample(Scene):
    def construct(self):
        # Color definitions
        COLOR_LAMBDA = YELLOW
        COLOR_DEGREE = ORANGE
        COLOR_RESULT = GREEN
        COLOR_HISTORY = GRAY_C

        # Title
        title = Text("Example: Verification of Homogeneity", font_size=35, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Container for the history elements in the top-left corner
        history = VGroup()

        # ----------------------------------------------------------------
        # STEP 1: Original Function
        # ----------------------------------------------------------------
        intro_text = Tex("Consider the function:", font_size=40)
        intro_text.move_to(UP * 1.8)
        
        func_orig = MathTex("f(x, y) = x^2 + 3xy")
        func_orig.next_to(intro_text, DOWN, buff=0.4)
        
        self.play(Write(intro_text))
        self.play(FadeIn(func_orig, shift=DOWN * 0.2))
        self.wait(1.5)

        # Create a scaled-down copy for the history corner
        hist_1 = func_orig.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_1.to_corner(UL).shift(DOWN * 1.2)
        history.add(hist_1)

        # Erase the center and show it in the corner simultaneously
        self.play(
            FadeOut(intro_text),
            FadeOut(func_orig),
            FadeIn(hist_1, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 2: Substitution
        # ----------------------------------------------------------------
        step1_text = Tex("Substitute $x \\rightarrow \\lambda x$ and $y \\rightarrow \\lambda y$:", font_size=40)
        step1_text.move_to(UP * 1.8)
        
        func_scaled = MathTex(
            "f(", "\\lambda", "x, ", "\\lambda", "y) = ", 
            "(", "\\lambda", "x)^2 + 3(", "\\lambda", "x)(", "\\lambda", "y)"
        )
        func_scaled.set_color_by_tex("\\lambda", COLOR_LAMBDA)
        func_scaled.next_to(step1_text, DOWN, buff=0.4)

        self.play(Write(step1_text))
        self.play(FadeIn(func_scaled, shift=DOWN * 0.2))
        self.wait(2)

        # Create a scaled-down copy for history
        hist_2 = func_scaled.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_2.next_to(hist_1, DOWN, buff=0.25).align_to(hist_1, LEFT)
        history.add(hist_2)

        # Erase the center and add to the corner history
        self.play(
            FadeOut(step1_text),
            FadeOut(func_scaled),
            FadeIn(hist_2, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 3: Expand
        # ----------------------------------------------------------------
        step2_text = Tex("Expand the powers and products:", font_size=40)
        step2_text.move_to(UP * 1.8)
        
        func_expanded = MathTex(
            "f(", "\\lambda", "x, ", "\\lambda", "y) = ", 
            "\\lambda^2", "x^2 + 3", "\\lambda^2", "xy"
        )
        func_expanded.set_color_by_tex("\\lambda", COLOR_LAMBDA)
        func_expanded.set_color_by_tex("\\lambda^2", COLOR_LAMBDA)
        func_expanded.next_to(step2_text, DOWN, buff=0.4)

        self.play(Write(step2_text))
        self.play(FadeIn(func_expanded, shift=DOWN * 0.2))
        self.wait(2)

        # Create a scaled-down copy for history
        hist_3 = func_expanded.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_3.next_to(hist_2, DOWN, buff=0.25).align_to(hist_2, LEFT)
        history.add(hist_3)

        # Erase the center and add to the corner history
        self.play(
            FadeOut(step2_text),
            FadeOut(func_expanded),
            FadeIn(hist_3, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 4: Factor Out
        # ----------------------------------------------------------------
        step3_text = Tex("Factor out $\\lambda^2$:", font_size=40)
        step3_text.move_to(UP * 1.8)
        
        func_final = MathTex(
            "f(", "\\lambda", "x, ", "\\lambda", "y) = ", 
            "\\lambda", "^2", "(x^2 + 3xy)"
        )
        func_final.set_color_by_tex("\\lambda", COLOR_LAMBDA)
        func_final.set_color_by_tex("^2", COLOR_DEGREE)
        func_final.next_to(step3_text, DOWN, buff=0.4)

        self.play(Write(step3_text))
        self.play(FadeIn(func_final, shift=DOWN * 0.2))
        self.wait(1.5)

        # ----------------------------------------------------------------
        # STEP 5: Conclusion
        # ----------------------------------------------------------------
        conclusion_text = Tex(
            r"Since $f(\lambda x, \lambda y) = \lambda^2 f(x,y)$, the function\\",
            r"is \textbf{homogeneous of degree 2}.",
            font_size=40
        )
        conclusion_text.set_color_by_tex("homogeneous of degree 2", COLOR_RESULT)
        conclusion_text.move_to(DOWN * 1.5)
        
        # Box around the original function component inside the final result
        box = SurroundingRectangle(func_final[5:], color=COLOR_RESULT, buff=0.15)
        
        self.play(Create(box))
        self.play(Write(conclusion_text))
        self.wait(3.5)

        # Smooth clean up of everything remaining on the screen
        self.play(
            FadeOut(title),
            FadeOut(step3_text),
            FadeOut(func_final),
            FadeOut(box),
            FadeOut(conclusion_text),
            FadeOut(history)
        )
        self.wait(1)
