%%manim -qm BernoulliEquationScene

from manim import *

class BernoulliEquationScene(Scene):
    def construct(self):
        # Color definitions
        COLOR_HIGHLIGHT = YELLOW
        COLOR_SUBST = ORANGE
        COLOR_RESULT = GREEN
        COLOR_HISTORY = GRAY_C

        # Title
        title = Text("The Bernoulli Differential Equation", font_size=32, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Container for the history elements in the top-left corner
        history = VGroup()

        # ----------------------------------------------------------------
        # STEP 1: Consider the Equation
        # ----------------------------------------------------------------
        step1_text = Tex("Consider the Bernoulli equation form:", font_size=40)
        step1_text.move_to(UP * 1.8)
        
        # Highlighting the non-linear part y^n
        eq_orig = MathTex("y' + P(x)y = Q(x)", "y^n")
        eq_orig[1].set_color(COLOR_SUBST)
        eq_orig.next_to(step1_text, DOWN, buff=0.4)
        
        self.play(Write(step1_text))
        self.play(FadeIn(eq_orig, shift=DOWN * 0.2))
        self.wait(2.5)

        # Move Initial Equation to history
        hist_1 = eq_orig.copy().scale(0.55).to_corner(UL).shift(DOWN * 1.2)
        history.add(hist_1)

        self.play(
            FadeOut(step1_text), 
            FadeOut(eq_orig), 
            FadeIn(hist_1, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 2: Divide by y^n
        # ----------------------------------------------------------------
        step2_text = Tex("Divide the entire equation by $y^n$ ($n \\neq 0, 1$):", font_size=40)
        step2_text.move_to(UP * 1.8)
        
        eq_divided = MathTex("y^{-n}y' + P(x)y^{1-n} = Q(x)")
        eq_divided.next_to(step2_text, DOWN, buff=0.4)
        
        self.play(Write(step2_text))
        self.play(FadeIn(eq_divided, shift=DOWN * 0.2))
        self.wait(2.5)

        # Move Step 2 to history
        hist_2 = eq_divided.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_2.next_to(hist_1, DOWN, buff=0.2).align_to(hist_1, LEFT)
        history.add(hist_2)

        self.play(FadeOut(step2_text), FadeOut(eq_divided), FadeIn(hist_2, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 3: Define the Substitution
        # ----------------------------------------------------------------
        step3_text = Tex("Introduce a new variable $z$ to linearize:", font_size=40)
        step3_text.move_to(UP * 1.8)
        
        eq_subst = MathTex("z = y^{1-n}")
        eq_subst.set_color(COLOR_SUBST)
        eq_subst.next_to(step3_text, DOWN, buff=0.4)

        self.play(Write(step3_text))
        self.play(FadeIn(eq_subst, shift=DOWN * 0.2))
        self.wait(2.0)

        # Move Step 3 to history
        hist_3 = eq_subst.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_3.next_to(hist_2, DOWN, buff=0.2).align_to(hist_2, LEFT)
        history.add(hist_3)

        self.play(FadeOut(step3_text), FadeOut(eq_subst), FadeIn(hist_3, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 4: Differentiate the Substitution
        # ----------------------------------------------------------------
        step4_text = Tex("Differentiate $z$ with respect to $x$ via Chain Rule:", font_size=40)
        step4_text.move_to(UP * 1.8)
        
        eq_diff = MathTex("z' = (1-n)y^{-n}y' \\implies \\frac{1}{1-n}z' = y^{-n}y'")
        eq_diff.set_color(COLOR_HIGHLIGHT)
        eq_diff.next_to(step4_text, DOWN, buff=0.4).scale(0.9)

        self.play(Write(step4_text))
        self.play(FadeIn(eq_diff, shift=DOWN * 0.2))
        self.wait(3.0)

        # Move Step 4 to history
        hist_4 = eq_diff.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_4.next_to(hist_3, DOWN, buff=0.2).align_to(hist_3, LEFT)
        history.add(hist_4)

        self.play(FadeOut(step4_text), FadeOut(eq_diff), FadeIn(hist_4, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 5: Final Canonical Linear Form
        # ----------------------------------------------------------------
        conclusion_text = Tex("Substitution transforms it into a \\textbf{Linear First-Order ODE}:", font_size=40)
        conclusion_text.set_color_by_tex("Linear First-Order ODE", COLOR_RESULT)
        conclusion_text.move_to(DOWN * 0.8)
        
        eq_final = MathTex("\\frac{1}{1-n}z' + P(x)z = Q(x)")
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
