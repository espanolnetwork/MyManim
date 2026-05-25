%%manim -qm ReduceToHomogeneousScene

from manim import *

class ReduceToHomogeneousScene(Scene):
    def construct(self):
        # Color definitions
        COLOR_HIGHLIGHT = YELLOW
        COLOR_SUBST = ORANGE
        COLOR_RESULT = GREEN
        COLOR_HISTORY = GRAY_C

        # Title
        title = Text("Equations Reducible to Homogeneous Form", font_size=32, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Container for the history elements in the top-left corner
        history = VGroup()

        # ----------------------------------------------------------------
        # STEP 1: Original Equation Form
        # ----------------------------------------------------------------
        step1_text = Tex("Consider the equation form:", font_size=40)
        step1_text.move_to(UP * 1.8)
        
        eq_orig = MathTex("y' = \\frac{ax + by + c}{a_1x + b_1y + c_1}")
        eq_orig.next_to(step1_text, DOWN, buff=0.4)
        
        self.play(Write(step1_text))
        self.play(FadeIn(eq_orig, shift=DOWN * 0.2))
        self.wait(2)

        # Create a scaled-down copy for the history corner
        hist_1 = eq_orig.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_1.to_corner(UL).shift(DOWN * 1.2)
        history.add(hist_1)

        # Erase the center and show it in the corner simultaneously
        self.play(
            FadeOut(step1_text),
            FadeOut(eq_orig),
            FadeIn(hist_1, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 2: Shift of Variables
        # ----------------------------------------------------------------
        step2_text = Tex("Translate coordinates to eliminate constants $c, c_1$:", font_size=40)
        step2_text.move_to(UP * 1.8)
        
        eq_subst = MathTex("x = u + \\alpha, \\quad y = v + \\beta")
        eq_subst.set_color(COLOR_SUBST)
        eq_subst.next_to(step2_text, DOWN, buff=0.4)

        self.play(Write(step2_text))
        self.play(FadeIn(eq_subst, shift=DOWN * 0.2))
        self.wait(2)

        # Create a scaled-down copy for history
        hist_2 = eq_subst.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_2.next_to(hist_1, DOWN, buff=0.25).align_to(hist_1, LEFT)
        history.add(hist_2)

        # Erase the center and add to the corner history
        self.play(
            FadeOut(step2_text),
            FadeOut(eq_subst),
            FadeIn(hist_2, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 3: Finding Alpha and Beta
        # ----------------------------------------------------------------
        step3_text = Tex("Find constants $\\alpha$ and $\\beta$ by solving the system:", font_size=40)
        step3_text.move_to(UP * 1.8)
        
        eq_system = MathTex(
            "\\begin{cases} "
            "a\\alpha + b\\beta + c = 0 \\\\ "
            "a_1\\alpha + b_1\\beta + c_1 = 0 "
            "\\end{cases}"
        )
        eq_system.set_color(COLOR_HIGHLIGHT)
        eq_system.next_to(step3_text, DOWN, buff=0.4)

        self.play(Write(step3_text))
        self.play(FadeIn(eq_system, shift=DOWN * 0.2))
        self.wait(2.5)

        # Create a scaled-down copy for history
        hist_3 = eq_system.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_3.next_to(hist_2, DOWN, buff=0.25).align_to(hist_2, LEFT)
        history.add(hist_3)

        # Erase the center and add to the corner history
        self.play(
            FadeOut(step3_text),
            FadeOut(eq_system),
            FadeIn(hist_3, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 4: Substitution Result
        # ----------------------------------------------------------------
        step4_text = Tex("Since $dx = du$ and $dy = dv$, the derivative is $v' = \\frac{dv}{du}$:", font_size=40)
        step4_text.move_to(UP * 1.8)
        
        eq_transformed = MathTex("v' = \\frac{a(u+\\alpha) + b(v+\\beta) + c}{a_1(u+\\alpha) + b_1(v+\\beta) + c_1}")
        eq_transformed.next_to(step4_text, DOWN, buff=0.4)

        self.play(Write(step4_text))
        self.play(FadeIn(eq_transformed, shift=DOWN * 0.2))
        self.wait(2.5)

        # Create a scaled-down copy for history
        hist_4 = eq_transformed.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_4.next_to(hist_3, DOWN, buff=0.25).align_to(hist_3, LEFT)
        history.add(hist_4)

        # Erase the center and add to the corner history
        self.play(
            FadeOut(step4_text),
            FadeOut(eq_transformed),
            FadeIn(hist_4, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 5: Final Result (Homogeneous Form)
        # ----------------------------------------------------------------
        conclusion_text = Tex("The system eliminates constants, yielding a \\textbf{homogeneous equation}:", font_size=40)
        conclusion_text.set_color_by_tex("homogeneous equation", COLOR_RESULT)
        conclusion_text.move_to(DOWN * 0.8)
        
        eq_final = MathTex("v' = \\frac{au + bv}{a_1u + b_1v}")
        eq_final.set_color(COLOR_RESULT)
        eq_final.next_to(conclusion_text, DOWN, buff=0.4)
        
        box = SurroundingRectangle(eq_final, color=COLOR_RESULT, buff=0.2)
        
        self.play(Write(conclusion_text))
        self.play(FadeIn(eq_final, shift=DOWN * 0.2))
        self.play(Create(box))
        self.wait(4)

        # Smooth clean up of everything remaining on the screen
        self.play(
            FadeOut(title),
            FadeOut(conclusion_text),
            FadeOut(eq_final),
            box.animate.scale(0).move_to(eq_final.get_center()),
            FadeOut(history)
        )
        self.wait(1)