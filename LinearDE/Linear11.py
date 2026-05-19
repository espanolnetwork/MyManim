%%manim -qm BernoulliExampleSolutionScene

from manim import *

class BernoulliExampleSolutionScene(Scene):
    def construct(self):
        # Color definitions
        COLOR_HIGHLIGHT = YELLOW
        COLOR_SUBST = ORANGE
        COLOR_RESULT = GREEN
        COLOR_HISTORY = GRAY_C

        # Title
        title = Text("Solving Bernoulli Equation", font_size=35, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Container for the history elements in the top-left corner
        history = VGroup()

        # ----------------------------------------------------------------
        # STEP 1: Consider the Initial Equation
        # ----------------------------------------------------------------
        step1_text = Tex("Consider the given Bernoulli equation:", font_size=40)
        step1_text.move_to(UP * 1.8)
        
        eq_orig = MathTex("(x + 1)y' - 2y = y^2(x + 1)^5")
        eq_orig.next_to(step1_text, DOWN, buff=0.4)
        
        self.play(Write(step1_text))
        self.play(FadeIn(eq_orig, shift=DOWN * 0.2))
        self.wait(2.0)

        # Move Initial Equation to history
        hist_1 = eq_orig.copy().scale(0.5).to_corner(UL).shift(DOWN * 1.2)
        history.add(hist_1)

        self.play(FadeOut(step1_text), FadeOut(eq_orig), FadeIn(hist_1, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 2: Divide by (x+1) and y^2
        # ----------------------------------------------------------------
        step2_text = Tex("Divide by $(x+1)$ and $y^2$ to isolate the $y^2$ term:", font_size=40)
        step2_text.move_to(UP * 1.8)
        
        eq_divided = MathTex("y^{-2}y' - \\frac{2}{x + 1}y^{-1} = (x + 1)^4")
        eq_divided.next_to(step2_text, DOWN, buff=0.4)
        
        self.play(Write(step2_text))
        self.play(FadeIn(eq_divided, shift=DOWN * 0.2))
        self.wait(2.5)

        # Move to history
        hist_2 = eq_divided.copy().scale(0.5).set_color(COLOR_HISTORY)
        hist_2.next_to(hist_1, DOWN, buff=0.2).align_to(hist_1, LEFT)
        history.add(hist_2)

        self.play(FadeOut(step2_text), FadeOut(eq_divided), FadeIn(hist_2, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 3: Change of Variable (z = y^-1)
        # ----------------------------------------------------------------
        step3_text = Tex("Introduce substitution $z = y^{-1} \\Rightarrow z' = -y^{-2}y'$:", font_size=40)
        step3_text.move_to(UP * 1.8)
        
        eq_subst = MathTex("-z' - \\frac{2}{x + 1}z = (x + 1)^4")
        eq_subst.set_color_by_tex("z", COLOR_SUBST)
        eq_subst.next_to(step3_text, DOWN, buff=0.4)

        self.play(Write(step3_text))
        self.play(FadeIn(eq_subst, shift=DOWN * 0.2))
        self.wait(2.5)

        # Move to history
        hist_3 = eq_subst.copy().scale(0.5).set_color(COLOR_HISTORY)
        hist_3.next_to(hist_2, DOWN, buff=0.2).align_to(hist_2, LEFT)
        history.add(hist_3)

        self.play(FadeOut(step3_text), FadeOut(eq_subst), FadeIn(hist_3, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 4: Standard Linear Form
        # ----------------------------------------------------------------
        step4_text = Tex("Multiply by $-1$ to get the standard linear form:", font_size=40)
        step4_text.move_to(UP * 1.8)
        
        eq_linear = MathTex("z' + \\frac{2}{x + 1}z = -(x + 1)^4")
        eq_linear.next_to(step4_text, DOWN, buff=0.4)

        self.play(Write(step4_text))
        self.play(FadeIn(eq_linear, shift=DOWN * 0.2))
        self.wait(2.0)

        # Move to history
        hist_4 = eq_linear.copy().scale(0.5).set_color(COLOR_HISTORY)
        hist_4.next_to(hist_3, DOWN, buff=0.2).align_to(hist_3, LEFT)
        history.add(hist_4)

        self.play(FadeOut(step4_text), FadeOut(eq_linear), FadeIn(hist_4, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 5: Solve for z(x) via Integrating Factor
        # ----------------------------------------------------------------
        step5_text = Tex("Solve the linear equation for $z(x)$:", font_size=40)
        step5_text.move_to(UP * 1.8)
        
        eq_solved_z = MathTex("z(x) = \\frac{1}{(x + 1)^2} \\left[ \\int -(x + 1)^6 dx \\right] = -\\frac{(x + 1)^5}{7} + \\frac{C}{(x + 1)^2}")
        eq_solved_z.set_color(COLOR_HIGHLIGHT)
        eq_solved_z.next_to(step5_text, DOWN, buff=0.4).scale(0.8)

        self.play(Write(step5_text))
        self.play(FadeIn(eq_solved_z, shift=DOWN * 0.2))
        self.wait(3.0)

        # Move to history
        hist_5 = eq_solved_z.copy().scale(0.5).set_color(COLOR_HISTORY)
        hist_5.next_to(hist_4, DOWN, buff=0.2).align_to(hist_4, LEFT)
        history.add(hist_5)

        self.play(FadeOut(step5_text), FadeOut(eq_solved_z), FadeIn(hist_5, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 6: Return to Original Variable y
        # ----------------------------------------------------------------
        conclusion_text = Tex("Substitute back $y = z^{-1}$ to find the final general solution:", font_size=40)
        conclusion_text.set_color_by_tex("final general solution", COLOR_RESULT)
        conclusion_text.move_to(DOWN * 0.8)
        
        eq_final = MathTex("y(x) = \\frac{7(x + 1)^2}{7C - (x + 1)^7}")
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