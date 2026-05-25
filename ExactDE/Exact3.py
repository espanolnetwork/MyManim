%%manim -qm ExactExampleSolutionScene2

from manim import *

class ExactExampleSolutionScene2(Scene):
    def construct(self):
        # Color definitions
        COLOR_HIGHLIGHT = YELLOW
        COLOR_SUBST = ORANGE
        COLOR_RESULT = GREEN
        COLOR_HISTORY = GRAY_C

        # Title
        title = Text("Solving Exact Equation: Another Example", font_size=35, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Container for the history elements in the top-left corner
        history = VGroup()

        # ----------------------------------------------------------------
        # STEP 1: Consider the Initial Equation
        # ----------------------------------------------------------------
        step1_text = Tex("Consider the given differential equation:", font_size=40)
        step1_text.move_to(UP * 1.8)
        
        eq_orig = MathTex("e^{-y}dx + (2 - xe^{-y})dy = 0")
        eq_orig.next_to(step1_text, DOWN, buff=0.4)
        
        self.play(Write(step1_text))
        self.play(FadeIn(eq_orig, shift=DOWN * 0.2))
        self.wait(2.0)

        # Move Initial Equation to history
        hist_1 = eq_orig.copy().scale(0.5).to_corner(UL).shift(DOWN * 1.2)
        history.add(hist_1)

        self.play(FadeOut(step1_text), FadeOut(eq_orig), FadeIn(hist_1, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 2: Verify Exactness Condition
        # ----------------------------------------------------------------
        step2_text = Tex("Check the exactness condition ($M_y = N_x$):", font_size=40)
        step2_text.move_to(UP * 1.8)
        
        eq_check = MathTex(
            "M = e^{-y} \\implies \\frac{\\partial M}{\\partial y} = -e^{-y}",
            "\\quad \\text{and} \\quad",
            "N = 2 - xe^{-y} \\implies \\frac{\\partial N}{\\partial x} = -e^{-y}"
        )
        eq_check.set_color(COLOR_HIGHLIGHT)
        eq_check.next_to(step2_text, DOWN, buff=0.4).scale(0.8)
        
        self.play(Write(step2_text))
        self.play(FadeIn(eq_check, shift=DOWN * 0.2))
        self.wait(2.5)

        # Move Step 2 to history
        hist_2 = eq_check.copy().scale(0.5).set_color(COLOR_HISTORY)
        hist_2.next_to(hist_1, DOWN, buff=0.2).align_to(hist_1, LEFT)
        history.add(hist_2)

        self.play(FadeOut(step2_text), FadeOut(eq_check), FadeIn(hist_2, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 3: Integrate M with respect to x
        # ----------------------------------------------------------------
        step3_text = Tex("Integrate $M(x,y)$ with respect to $x$ to find $U(x,y)$:", font_size=40)
        step3_text.move_to(UP * 1.8)
        
        eq_integrate = MathTex("U(x, y) = \\int e^{-y}dx = xe^{-y} + h(y)")
        eq_integrate.set_color(COLOR_SUBST)
        eq_integrate.next_to(step3_text, DOWN, buff=0.4)

        self.play(Write(step3_text))
        self.play(FadeIn(eq_integrate, shift=DOWN * 0.2))
        self.wait(2.5)

        # Move Step 3 to history
        hist_3 = eq_integrate.copy().scale(0.5).set_color(COLOR_HISTORY)
        hist_3.next_to(hist_2, DOWN, buff=0.2).align_to(hist_2, LEFT)
        history.add(hist_3)

        self.play(FadeOut(step3_text), FadeOut(eq_integrate), FadeIn(hist_3, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 4: Differentiate U with respect to y
        # ----------------------------------------------------------------
        step4_text = Tex("Differentiate $U$ by $y$ and equate to $N(x,y)$:", font_size=40)
        step4_text.move_to(UP * 1.8)
        
        eq_find_h = MathTex("\\frac{\\partial U}{\\partial y} = -xe^{-y} + h'(y) = 2 - xe^{-y} \\implies h'(y) = 2")
        eq_find_h.next_to(step4_text, DOWN, buff=0.4).scale(0.8)

        self.play(Write(step4_text))
        self.play(FadeIn(eq_find_h, shift=DOWN * 0.2))
        self.wait(2.5)

        # Move Step 4 to history
        hist_4 = eq_find_h.copy().scale(0.5).set_color(COLOR_HISTORY)
        hist_4.next_to(hist_3, DOWN, buff=0.2).align_to(hist_3, LEFT)
        history.add(hist_4)

        self.play(FadeOut(step4_text), FadeOut(eq_find_h), FadeIn(hist_4, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 5: Find h(y)
        # ----------------------------------------------------------------
        step5_text = Tex("Integrate $h'(y)$ to find the function $h(y)$:", font_size=40)
        step5_text.move_to(UP * 1.8)

        eq_h_final = MathTex("h(y) = \\int 2 \\, dy = 2y")
        eq_h_final.set_color(COLOR_HIGHLIGHT)
        eq_h_final.next_to(step5_text, DOWN, buff=0.4)
        
        self.play(Write(step5_text))
        self.play(FadeIn(eq_h_final, shift=DOWN * 0.2))
        self.wait(2.0)

        # Move Step 5 to history
        hist_5 = eq_h_final.copy().scale(0.5).set_color(COLOR_HISTORY)
        hist_5.next_to(hist_4, DOWN, buff=0.2).align_to(hist_4, LEFT)
        history.add(hist_5)

        self.play(FadeOut(step5_text), FadeOut(eq_h_final), FadeIn(hist_5, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 6: Conclusion (General Solution)
        # ----------------------------------------------------------------
        conclusion_text = Tex("Combine terms for the implicit \\textbf{general solution}:", font_size=40)
        conclusion_text.set_color_by_tex("general solution", COLOR_RESULT)
        conclusion_text.move_to(DOWN * 0.8)
        
        eq_final = MathTex("xe^{-y} + 2y = C")
        eq_final.set_color(COLOR_RESULT)
        eq_final.next_to(conclusion_text, DOWN, buff=0.4)
        
        box = SurroundingRectangle(eq_final, color=COLOR_RESULT, buff=0.2)
        
        self.play(Write(conclusion_text))
        self.play(FadeIn(eq_final, shift=DOWN * 0.2))
        self.play(Create(box))
        self.wait(4.0)

        # Final clean up
        self.play(
            FadeOut(title), FadeOut(conclusion_text), FadeOut(eq_final),
            box.animate.scale(0).move_to(eq_final.get_center()), FadeOut(history)
        )
        self.wait(1)