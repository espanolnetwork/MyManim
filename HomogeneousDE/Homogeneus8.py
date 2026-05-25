%%manim -qm SolveReducibleExampleScene

from manim import *

class SolveReducibleExampleScene(Scene):
    def construct(self):
        # Color definitions
        COLOR_HIGHLIGHT = YELLOW
        COLOR_SUBST = ORANGE
        COLOR_RESULT = GREEN
        COLOR_HISTORY = GRAY_C

        # Title
        title = Text("Example: Solving Reducible Equation", font_size=32, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Container for the history elements in the top-left corner
        history = VGroup()

        # ----------------------------------------------------------------
        # STEP 1: Consider the Equation
        # ----------------------------------------------------------------
        step1_text = Tex("Consider the equation:", font_size=40)
        step1_text.move_to(UP * 1.8)
        
        eq_orig = MathTex("y' = \\frac{x + y - 1}{x - y + 3}")
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
        # STEP 2: Find Alpha and Beta
        # ----------------------------------------------------------------
        step2_text = Tex("Find $\\alpha$ and $\\beta$ by setting the expressions to 0:", font_size=40)
        step2_text.move_to(UP * 1.8)
        
        eq_system = MathTex(
            "\\begin{cases} "
            "\\alpha + \\beta - 1 = 0 \\\\ "
            "\\alpha - \\beta + 3 = 0 "
            "\\end{cases}"
        )
        eq_system.set_color(COLOR_HIGHLIGHT)
        eq_system.next_to(step2_text, DOWN, buff=0.4)

        self.play(Write(step2_text))
        self.play(FadeIn(eq_system, shift=DOWN * 0.2))
        self.wait(2.5)

        # Create a scaled-down copy for history
        hist_2 = eq_system.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_2.next_to(hist_1, DOWN, buff=0.25).align_to(hist_1, LEFT)
        history.add(hist_2)

        # Erase the center and add to the corner history
        self.play(
            FadeOut(step2_text),
            FadeOut(eq_system),
            FadeIn(hist_2, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 3: System Solution
        # ----------------------------------------------------------------
        step3_text = Tex("Solving the linear system yields:", font_size=40)
        step3_text.move_to(UP * 1.8)
        
        eq_solution = MathTex("\\alpha = -1, \\quad \\beta = 2")
        eq_solution.set_color(COLOR_HIGHLIGHT)
        eq_solution.next_to(step3_text, DOWN, buff=0.4)

        self.play(Write(step3_text))
        self.play(FadeIn(eq_solution, shift=DOWN * 0.2))
        self.wait(2)

        # Create a scaled-down copy for history
        hist_3 = eq_solution.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_3.next_to(hist_2, DOWN, buff=0.25).align_to(hist_2, LEFT)
        history.add(hist_3)

        # Erase the center and add to the corner history
        self.play(
            FadeOut(step3_text),
            FadeOut(eq_solution),
            FadeIn(hist_3, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 4: Apply Shift Transformations
        # ----------------------------------------------------------------
        step4_text = Tex("Apply the change of variables:", font_size=40)
        step4_text.move_to(UP * 1.8)
        
        eq_transform = MathTex("x = u - 1, \\quad y = v + 2")
        eq_transform.set_color(COLOR_SUBST)
        eq_transform.next_to(step4_text, DOWN, buff=0.4)

        self.play(Write(step4_text))
        self.play(FadeIn(eq_transform, shift=DOWN * 0.2))
        self.wait(2)

        # Create a scaled-down copy for history
        hist_4 = eq_transform.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_4.next_to(hist_3, DOWN, buff=0.25).align_to(hist_3, LEFT)
        history.add(hist_4)

        # Erase the center and add to the corner history
        self.play(
            FadeOut(step4_text),
            FadeOut(eq_transform),
            FadeIn(hist_4, shift=UP * 0.2)
        )

        # ----------------------------------------------------------------
        # STEP 5: Final Reduced Form
        # ----------------------------------------------------------------
        conclusion_text = Tex("The constant terms cancel out, leaving a \\textbf{homogeneous form}:", font_size=40)
        conclusion_text.set_color_by_tex("homogeneous form", COLOR_RESULT)
        conclusion_text.move_to(DOWN * 0.8)
        
        eq_final = MathTex("v' = \\frac{u + v}{u - v}")
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
