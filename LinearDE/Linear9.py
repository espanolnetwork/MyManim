%%manim -qm LinearInvertedDEScene

from manim import *

class LinearInvertedDEScene(Scene):
    def construct(self):
        # Color definitions
        COLOR_HIGHLIGHT = YELLOW
        COLOR_SUBST = ORANGE
        COLOR_RESULT = GREEN
        COLOR_HISTORY = GRAY_C

        # Main Title
        title = Text("Solving via x = x(y)", font_size=35, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Container for the history elements in the top-left corner
        history = VGroup()

        # ----------------------------------------------------------------
        # NEW STEP: Consider the Initial Equation
        # ----------------------------------------------------------------
        step_init_text = Tex("Consider the equation:", font_size=40)
        step_init_text.move_to(UP * 1.8)
        
        eq_initial = MathTex("y^2 dx + (x + 2)dy = 0")
        eq_initial.next_to(step_init_text, DOWN, buff=0.4)
        
        self.play(Write(step_init_text))
        self.play(FadeIn(eq_initial, shift=DOWN * 0.2))
        self.wait(2.0)

        # Move Initial Equation to history
        hist_0 = eq_initial.copy().scale(0.5).to_corner(UL).shift(DOWN * 1.2)
        history.add(hist_0)

        self.play(
            FadeOut(step_init_text), 
            FadeOut(eq_initial), 
            FadeIn(hist_0, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 1: Invert the derivative
        # ----------------------------------------------------------------
        step1_text = Tex("Divide by $dy$ and rewrite as $x = x(y)$:", font_size=40)
        step1_text.move_to(UP * 1.8)
        
        eq_orig = MathTex("y^2 \\frac{dx}{dy} + x = -2 \\implies x' + \\frac{1}{y^2}x = -\\frac{2}{y^2}")
        eq_orig.next_to(step1_text, DOWN, buff=0.4).scale(0.85)
        
        self.play(Write(step1_text))
        self.play(FadeIn(eq_orig, shift=DOWN * 0.2))
        self.wait(2.5)

        # Move Step 1 to history below the initial equation
        hist_1 = eq_orig.copy().scale(0.5).set_color(COLOR_HISTORY)
        hist_1.next_to(hist_0, DOWN, buff=0.2).align_to(hist_0, LEFT)
        history.add(hist_1)

        self.play(FadeOut(step1_text), FadeOut(eq_orig), FadeIn(hist_1, shift=UP * 0.2))

        # ================================================================
        # METHOD 1: BERNOULLI METHOD (x = u * v)
        # ================================================================
        m1_title = Tex("\\textbf{Method 1: Bernoulli} ($x = u \\cdot v \\Rightarrow x' = u'v + uv'$):", font_size=36, color=ORANGE)
        m1_title.move_to(UP * 1.8)
        self.play(Write(m1_title))
        self.wait(1.5)
        self.play(FadeOut(m1_title))

        # STEP 2: Substitute x = uv
        step2_text = Tex("Substitute $x = uv$ into the linear ODE form:", font_size=40)
        step2_text.move_to(UP * 1.8)
        
        eq_subst = MathTex("u'v + uv' + \\frac{1}{y^2}(uv) = -\\frac{2}{y^2}")
        eq_subst.set_color_by_tex("uv", COLOR_SUBST)
        eq_subst.next_to(step2_text, DOWN, buff=0.4)

        self.play(Write(step2_text))
        self.play(FadeIn(eq_subst, shift=DOWN * 0.2))
        self.wait(2)

        # Move to history
        hist_2 = eq_subst.copy().scale(0.5).set_color(COLOR_HISTORY)
        hist_2.next_to(hist_1, DOWN, buff=0.2).align_to(hist_1, LEFT)
        history.add(hist_2)

        self.play(FadeOut(step2_text), FadeOut(eq_subst), FadeIn(hist_2, shift=UP * 0.2))

        # STEP 3: Group and Find v(y)
        step3_text = Tex("Group terms and solve $v' + \\frac{1}{y^2}v = 0$ for $v(y)$:", font_size=40)
        step3_text.move_to(UP * 1.8)
        
        eq_find_v = MathTex("\\frac{dv}{v} = -\\frac{dy}{y^2} \\implies \\ln|v| = \\frac{1}{y} \\implies v = e^{1/y}")
        eq_find_v.set_color(COLOR_HIGHLIGHT)
        eq_find_v.next_to(step3_text, DOWN, buff=0.4).scale(0.85)

        self.play(Write(step3_text))
        self.play(FadeIn(eq_find_v, shift=DOWN * 0.2))
        self.wait(2.5)

        # Move to history
        hist_3 = eq_find_v.copy().scale(0.5).set_color(COLOR_HISTORY)
        hist_3.next_to(hist_2, DOWN, buff=0.2).align_to(hist_2, LEFT)
        history.add(hist_3)

        self.play(FadeOut(step3_text), FadeOut(eq_find_v), FadeIn(hist_3, shift=UP * 0.2))

        # STEP 4: Find u(y)
        step4_text = Tex("Solve the remaining part $u'v = -\\frac{2}{y^2}$ for $u(y)$:", font_size=40)
        step4_text.move_to(UP * 1.8)

        eq_find_u = MathTex("u'e^{1/y} = -\\frac{2}{y^2} \\implies u = \\int -\\frac{2}{y^2}e^{-1/y}dy = 2e^{-1/y} + C")
        eq_find_u.set_color(COLOR_HIGHLIGHT)
        eq_find_u.next_to(step4_text, DOWN, buff=0.4).scale(0.8)
        
        self.play(Write(step4_text))
        self.play(FadeIn(eq_find_u, shift=DOWN * 0.2))
        self.wait(3)

        # Move to history
        hist_4 = eq_find_u.copy().scale(0.5).set_color(COLOR_HISTORY)
        hist_4.next_to(hist_3, DOWN, buff=0.2).align_to(hist_3, LEFT)
        history.add(hist_4)

        self.play(FadeOut(step4_text), FadeOut(eq_find_u), FadeIn(hist_4, shift=UP * 0.2))

        # STEP 5: Method 1 Conclusion
        step5_text = Tex("Combine $u$ and $v$ to get the general solution $x(y)$:", font_size=40)
        step5_text.move_to(UP * 1.8)

        eq_sol_m1 = MathTex("x = (2e^{-1/y} + C)e^{1/y} \\implies x = 2 + Ce^{1/y}")
        eq_sol_m1.set_color(COLOR_RESULT)
        eq_sol_m1.next_to(step5_text, DOWN, buff=0.4)

        self.play(Write(step5_text))
        self.play(FadeIn(eq_sol_m1, shift=DOWN * 0.2))
        self.wait(2.5)

        # Clean history and center for Lagrange demonstration
        self.play(FadeOut(step5_text), FadeOut(eq_sol_m1), FadeOut(history))
        history = VGroup() # Reset history stack

        # ================================================================
        # METHOD 2: LAGRANGE METHOD (Variation of Parameter)
        # ================================================================
        m2_title = Tex("\\textbf{Method 2: Lagrange} (Variation of Parameters):", font_size=36, color=YELLOW)
        m2_title.move_to(UP * 1.8)
        self.play(Write(m2_title))
        self.wait(1.5)
        self.play(FadeOut(m2_title))

        # STEP 6: Homogeneous solution
        step6_text = Tex("First, solve the homogeneous equation $x' + \\frac{1}{y^2}x = 0$:", font_size=40)
        step6_text.move_to(UP * 1.8)

        eq_hom = MathTex("x_h = C \\cdot e^{-\\int \\frac{1}{y^2}dy} \\implies x_h = C \\cdot e^{1/y}")
        eq_hom.set_color(COLOR_HIGHLIGHT)
        eq_hom.next_to(step6_text, DOWN, buff=0.4)

        self.play(Write(step6_text))
        self.play(FadeIn(eq_hom, shift=DOWN * 0.2))
        self.wait(2)

        # Move to history
        hist_5 = eq_hom.copy().scale(0.5).to_corner(UL).shift(DOWN * 1.2)
        history.add(hist_5)

        self.play(FadeOut(step6_text), FadeOut(eq_hom), FadeIn(hist_5, shift=UP * 0.2))

        # STEP 7: Vary the constant
        step7_text = Tex("Vary the constant: Let $C = C(y)$:", font_size=40)
        step7_text.move_to(UP * 1.8)

        eq_vary = MathTex("x = C(y)e^{1/y} \\implies x' = C'(y)e^{1/y} - \\frac{1}{y^2}C(y)e^{1/y}")
        eq_vary.set_color(COLOR_SUBST)
        eq_vary.next_to(step7_text, DOWN, buff=0.4).scale(0.8)

        self.play(Write(step7_text))
        self.play(FadeIn(eq_vary, shift=DOWN * 0.2))
        self.wait(2.5)

        # Move to history
        hist_6 = eq_vary.copy().scale(0.5).next_to(hist_5, DOWN, buff=0.2).align_to(hist_5, LEFT)
        history.add(hist_6)

        self.play(FadeOut(step7_text), FadeOut(eq_vary), FadeIn(hist_6, shift=UP * 0.2))

        # STEP 8: Substitute back and solve for C'(y)
        step8_text = Tex("Substitute back into original ODE and solve for $C'(y)$:", font_size=40)
        step8_text.move_to(UP * 1.8)

        eq_find_c = MathTex("C'(y)e^{1/y} = -\\frac{2}{y^2} \\implies C(y) = \\int -\\frac{2}{y^2}e^{-1/y}dy = 2e^{-1/y} + C")
        eq_find_c.set_color(COLOR_HIGHLIGHT)
        eq_find_c.next_to(step8_text, DOWN, buff=0.4).scale(0.8)

        self.play(Write(step8_text))
        self.play(FadeIn(eq_find_c, shift=DOWN * 0.2))
        self.wait(3)

        # Move to history
        hist_7 = eq_find_c.copy().scale(0.5).next_to(hist_6, DOWN, buff=0.2).align_to(hist_6, LEFT)
        history.add(hist_7)

        self.play(FadeOut(step8_text), FadeOut(eq_find_c), FadeIn(hist_7, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # FINAL STEP: General Solution Conclusion
        # ----------------------------------------------------------------
        conclusion_text = Tex("Both methods yield the same \\textbf{general solution} $x(y)$:", font_size=40)
        conclusion_text.set_color_by_tex("general solution", COLOR_RESULT)
        conclusion_text.move_to(DOWN * 0.8)
        
        eq_final = MathTex("x(y) = 2 + C \\cdot e^{1/y}")
        eq_final.set_color(COLOR_RESULT)
        eq_final.next_to(conclusion_text, DOWN, buff=0.4)
        
        box = SurroundingRectangle(eq_final, color=COLOR_RESULT, buff=0.2)
        
        self.play(Write(conclusion_text))
        self.play(FadeIn(eq_final, shift=DOWN * 0.2))
        self.play(Create(box))
        self.wait(4)

        # Final clean up
        self.play(
            FadeOut(title), FadeOut(conclusion_text), FadeOut(eq_final),
            box.animate.scale(0).move_to(eq_final.get_center()), FadeOut(history)
        )
        self.wait(1)