%%manim -qm SolveHomogeneousPartScene

from manim import *

class SolveHomogeneousPartScene(Scene):
    def construct(self):
        # Color definitions
        COLOR_HIGHLIGHT = YELLOW
        COLOR_SUBST = ORANGE
        COLOR_RESULT = GREEN
        COLOR_HISTORY = GRAY_C

        # Title
        title = Text("Now solving the Reduced Homogeneous Equation", font_size=35, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Container for the history elements in the top-left corner
        history = VGroup()

        # ----------------------------------------------------------------
        # STEP 1: Current Equation
        # ----------------------------------------------------------------
        step1_text = Tex("Consider the equation from the previous step:", font_size=40)
        step1_text.move_to(UP * 1.8)
        
        eq_orig = MathTex("v' = \\frac{u + v}{u - v}")
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
        # STEP 2: Substitution v = zu
        # ----------------------------------------------------------------
        step2_text = Tex("Apply substitution: $v = zu \\Rightarrow v' = z + u z'$:", font_size=40)
        step2_text.move_to(UP * 1.8)
        
        eq_subst = MathTex("z + u z' = \\frac{u + (zu)}{u - (zu)}")
        eq_subst.set_color_by_tex("zu", COLOR_SUBST)
        eq_subst.set_color_by_tex("z + u z'", COLOR_SUBST)
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
        # STEP 3: Simplify Fraction
        # ----------------------------------------------------------------
        step3_text = Tex("Factor out and cancel $u$ from the fraction:", font_size=40)
        step3_text.move_to(UP * 1.8)
        
        eq_simplified = MathTex("z + u z' = \\frac{1 + z}{1 - z}")
        eq_simplified.next_to(step3_text, DOWN, buff=0.4)

        self.play(Write(step3_text))
        self.play(FadeIn(eq_simplified, shift=DOWN * 0.2))
        self.wait(2)

        # Create a scaled-down copy for history
        hist_3 = eq_simplified.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_3.next_to(hist_2, DOWN, buff=0.25).align_to(hist_2, LEFT)
        history.add(hist_3)

        # Erase the center and add to the corner history
        self.play(
            FadeOut(step3_text),
            FadeOut(eq_simplified),
            FadeIn(hist_3, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 4: Move z to Right Side
        # ----------------------------------------------------------------
        step4_text = Tex("Isolate the derivative term by moving $z$:", font_size=40)
        step4_text.move_to(UP * 1.8)
        
        eq_move_z = MathTex("u z' = \\frac{1 + z}{1 - z} - z")
        eq_move_z.next_to(step4_text, DOWN, buff=0.4)

        self.play(Write(step4_text))
        self.play(FadeIn(eq_move_z, shift=DOWN * 0.2))
        self.wait(2)

        # Create a scaled-down copy for history
        hist_4 = eq_move_z.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_4.next_to(hist_3, DOWN, buff=0.25).align_to(hist_3, LEFT)
        history.add(hist_4)

        # Erase the center and add to the corner history
        self.play(
            FadeOut(step4_text),
            FadeOut(eq_move_z),
            FadeIn(hist_4, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 5: Common Denominator
        # ----------------------------------------------------------------
        step5_text = Tex("Find a common denominator on the right:", font_size=40)
        step5_text.move_to(UP * 1.8)

        eq_common = MathTex("u \\frac{dz}{du} = \\frac{1 + z^2}{1 - z}")
        eq_common.next_to(step5_text, DOWN, buff=0.4)
        
        self.play(Write(step5_text))
        self.play(FadeIn(eq_common, shift=DOWN * 0.2))
        self.wait(2)

        # Create a scaled-down copy for history
        hist_5 = eq_common.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_5.next_to(hist_4, DOWN, buff=0.25).align_to(hist_4, LEFT)
        history.add(hist_5)

        # Erase the center and add to the corner history
        self.play(
            FadeOut(step5_text),
            FadeOut(eq_common),
            FadeIn(hist_5, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 6: Conclusion (Separated Variables)
        # ----------------------------------------------------------------
        conclusion_text = Tex("Separate variables to prepare for integration:", font_size=40)
        conclusion_text.set_color_by_tex("Separate variables", COLOR_RESULT)
        conclusion_text.move_to(DOWN * 0.8)
        
        eq_separable = MathTex("\\frac{1 - z}{1 + z^2} dz = \\frac{1}{u} du")
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
            FadeOut(conclusion_text),
            FadeOut(eq_separable),
            box.animate.scale(0).move_to(eq_separable.get_center()),
            FadeOut(history)
        )
        self.wait(1)