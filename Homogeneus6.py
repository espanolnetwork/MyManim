%%manim -qm HomogeneousDESolution2

from manim import *

class HomogeneousDESolution2(Scene):
    def construct(self):
        # Color definitions
        COLOR_HIGHLIGHT = YELLOW
        COLOR_SUBST = ORANGE
        COLOR_RESULT = GREEN
        COLOR_HISTORY = GRAY_C

        # Title
        title = Text("Solving Homogeneous DE", font_size=32, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Container for the history elements in the top-left corner
        history = VGroup()

        # ----------------------------------------------------------------
        # STEP 1: Original Equation
        # ----------------------------------------------------------------
        step1_text = Tex("Consider the equation:", font_size=40)
        step1_text.move_to(UP * 1.8)
        
        eq_orig = MathTex("y - x", "y'", " = y \\ln\\left(\\frac{y}{x}\\right)")
        eq_orig.next_to(step1_text, DOWN, buff=0.4)
        
        self.play(Write(step1_text))
        self.play(FadeIn(eq_orig, shift=DOWN * 0.2))
        self.wait(1.5)

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
        # STEP 2: Substitution
        # ----------------------------------------------------------------
        step2_text = Tex("Apply substitution: $y = ux \\Rightarrow y' = u + x u'$:", font_size=40)
        step2_text.move_to(UP * 1.8)
        
        eq_subst = MathTex("(ux) - x", "(u + x u')", " = (ux) \\ln\\left(\\frac{ux}{x}\\right)")
        eq_subst.set_color_by_tex("ux", COLOR_SUBST)
        eq_subst.set_color_by_tex("(u + x u')", COLOR_SUBST)
        eq_subst.next_to(step2_text, DOWN, buff=0.4)

        self.play(Write(step2_text))
        self.play(FadeIn(eq_subst, shift=DOWN * 0.2))
        self.wait(2.5)

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
        # STEP 3: Simplify and Expand
        # ----------------------------------------------------------------
        step3_text = Tex("Simplify the logarithm and expand terms:", font_size=40)
        step3_text.move_to(UP * 1.8)
        
        eq_expanded = MathTex("ux - xu - x^2 u'", " = ux \\ln(u)")
        eq_expanded.next_to(step3_text, DOWN, buff=0.4)

        self.play(Write(step3_text))
        self.play(FadeIn(eq_expanded, shift=DOWN * 0.2))
        self.wait(2)

        # Create a scaled-down copy for history
        hist_3 = eq_expanded.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_3.next_to(hist_2, DOWN, buff=0.25).align_to(hist_2, LEFT)
        history.add(hist_3)

        # Erase the center and add to the corner history
        self.play(
            FadeOut(step3_text),
            FadeOut(eq_expanded),
            FadeIn(hist_3, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 4: Cancel Terms
        # ----------------------------------------------------------------
        step4_text = Tex("Cancel $ux$ and $-xu$ on the left side:", font_size=40)
        step4_text.move_to(UP * 1.8)
        
        eq_canceled = MathTex("-x^2 u'", " = ux \\ln(u)")
        eq_canceled.next_to(step4_text, DOWN, buff=0.4)

        self.play(Write(step4_text))
        self.play(FadeIn(eq_canceled, shift=DOWN * 0.2))
        self.wait(2)

        # Create a scaled-down copy for history
        hist_4 = eq_canceled.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_4.next_to(hist_3, DOWN, buff=0.25).align_to(hist_3, LEFT)
        history.add(hist_4)

        # Erase the center and add to the corner history
        self.play(
            FadeOut(step4_text),
            FadeOut(eq_canceled),
            FadeIn(hist_4, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 5: Express Derivative as Differential
        # ----------------------------------------------------------------
        step5_text = Tex("Rewrite $u'$ as $du / dx$ and rearrange:", font_size=40)
        step5_text.move_to(UP * 1.8)

        eq_final = MathTex("-x^2 \\frac{du}{dx}", " = ux \\ln(u)")
        eq_final.next_to(step5_text, DOWN, buff=0.4)
        
        self.play(Write(step5_text))
        self.play(FadeIn(eq_final, shift=DOWN * 0.2))
        self.wait(1.5)

        # ----------------------------------------------------------------
        # STEP 6: Conclusion (Separated Form)
        # ----------------------------------------------------------------
        conclusion_text = Tex("Divide by $x^2 u \\ln(u)$ to get the \\textbf{separable form}:", font_size=40)
        conclusion_text.set_color_by_tex("separable form", COLOR_RESULT)
        conclusion_text.move_to(DOWN * 0.8)
        
        eq_separable = MathTex("\\frac{1}{u \\ln(u)} du = -\\frac{1}{x} dx")
        eq_separable.set_color(COLOR_RESULT)
        eq_separable.next_to(conclusion_text, DOWN, buff=0.4)
        
        box = SurroundingRectangle(eq_separable, color=COLOR_RESULT, buff=0.2)
        
        self.play(Write(conclusion_text))
        self.play(FadeIn(eq_separable, shift=DOWN * 0.2))
        self.play(Create(box))
        self.wait(4)

        # Smooth clean up of everything remaining on the screen
        self.play(
            FadeOut(title),
            FadeOut(step5_text),
            FadeOut(eq_final),
            FadeOut(conclusion_text),
            FadeOut(eq_separable),
            FadeOut(box),
            FadeOut(history)
        )
        self.wait(1)
