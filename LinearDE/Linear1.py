%%manim -qm LinearOrderNDEScene

from manim import *

class LinearOrderNDEScene(Scene):
    def construct(self):
        # Color definitions
        COLOR_HIGHLIGHT = YELLOW
        COLOR_SUBST = ORANGE
        COLOR_RESULT = GREEN
        COLOR_HISTORY = GRAY_C

        # Title
        title = Text("Linear Ordinary Differential Equations", font_size=32, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Container for the history elements in the top-left corner
        history = VGroup()

        # ----------------------------------------------------------------
        # STEP 1: General n-th Order Standard Form
        # ----------------------------------------------------------------
        step1_text = Tex("General Standard Form of an $n$-th order linear ODE:", font_size=40)
        step1_text.move_to(UP * 1.8)
        
        eq_orig = MathTex(
            "a_n(x)y^{(n)} + a_{n-1}(x)y^{(n-1)} + \\dots + a_1(x)y' + a_0(x)y = g(x)"
        )
        eq_orig.next_to(step1_text, DOWN, buff=0.4).scale(0.85) # slightly scale to fit screen width
        
        self.play(Write(step1_text))
        self.play(FadeIn(eq_orig, shift=DOWN * 0.2))
        self.wait(2.5)

        # Create a scaled-down copy for the history corner
        hist_1 = eq_orig.copy().scale(0.5).set_color(COLOR_HISTORY)
        hist_1.to_corner(UL).shift(DOWN * 1.2)
        history.add(hist_1)

        # Erase the center and show it in the corner simultaneously
        self.play(
            FadeOut(step1_text),
            FadeOut(eq_orig),
            FadeIn(hist_1, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 2: Definition for n = 1
        # ----------------------------------------------------------------
        step2_text = Tex("As a subset, define the first-order case ($n=1$):", font_size=40)
        step2_text.move_to(UP * 1.8)
        
        eq_first_order = MathTex("a_1(x)y' + a_0(x)y = g(x)")
        eq_first_order.set_color(COLOR_HIGHLIGHT)
        eq_first_order.next_to(step2_text, DOWN, buff=0.4)

        self.play(Write(step2_text))
        self.play(FadeIn(eq_first_order, shift=DOWN * 0.2))
        self.wait(2)

        # Create a scaled-down copy for history
        hist_2 = eq_first_order.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_2.next_to(hist_1, DOWN, buff=0.25).align_to(hist_1, LEFT)
        history.add(hist_2)

        # Erase the center and add to the corner history
        self.play(
            FadeOut(step2_text),
            FadeOut(eq_first_order),
            FadeIn(hist_2, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 3: Division by Leading Coefficient
        # ----------------------------------------------------------------
        step3_text = Tex("Divide by the leading coefficient $a_1(x)$ (where $a_1(x) \\neq 0$):", font_size=40)
        step3_text.move_to(UP * 1.8)
        
        eq_divided = MathTex("y' + \\frac{a_0(x)}{a_1(x)}y = \\frac{g(x)}{a_1(x)}")
        eq_divided.next_to(step3_text, DOWN, buff=0.4)

        self.play(Write(step3_text))
        self.play(FadeIn(eq_divided, shift=DOWN * 0.2))
        self.wait(2.5)

        # Create a scaled-down copy for history
        hist_3 = eq_divided.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_3.next_to(hist_2, DOWN, buff=0.25).align_to(hist_2, LEFT)
        history.add(hist_3)

        # Erase the center and add to the corner history
        self.play(
            FadeOut(step3_text),
            FadeOut(eq_divided),
            FadeIn(hist_3, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 4: Standard Form Substitution Notation
        # ----------------------------------------------------------------
        step4_text = Tex("Let $P(x) = \\frac{a_0(x)}{a_1(x)}$ and $Q(x) = \\frac{g(x)}{a_1(x)}$:", font_size=40)
        step4_text.move_to(UP * 1.8)
        
        eq_subst_notation = MathTex("P(x) \\quad \\text{and} \\quad Q(x)")
        eq_subst_notation.set_color(COLOR_SUBST)
        eq_subst_notation.next_to(step4_text, DOWN, buff=0.4)

        self.play(Write(step4_text))
        self.play(FadeIn(eq_subst_notation, shift=DOWN * 0.2))
        self.wait(2)

        # Create a scaled-down copy for history
        hist_4 = eq_subst_notation.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_4.next_to(hist_3, DOWN, buff=0.25).align_to(hist_3, LEFT)
        history.add(hist_4)

        # Erase the center and add to the corner history
        self.play(
            FadeOut(step4_text),
            FadeOut(eq_subst_notation),
            FadeIn(hist_4, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 5: Final Canonical First-Order Form
        # ----------------------------------------------------------------
        conclusion_text = Tex("This yields the standard canonical form for \\textbf{Linear First-Order ODEs}:", font_size=40)
        conclusion_text.set_color_by_tex("Linear First-Order ODEs", COLOR_RESULT)
        conclusion_text.move_to(DOWN * 0.8)
        
        eq_final = MathTex("y' + P(x)y = Q(x)")
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
