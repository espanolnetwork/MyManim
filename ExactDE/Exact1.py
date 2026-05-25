%%manim -qm ExactEquationTheoryScene

from manim import *

class ExactEquationTheoryScene(Scene):
    def construct(self):
        # Color definitions
        COLOR_HIGHLIGHT = YELLOW
        COLOR_SUBST = ORANGE
        COLOR_RESULT = GREEN
        COLOR_HISTORY = GRAY_C

        # Title
        title = Text("Exact Differential Equations", font_size=35, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Container for the history elements in the top-left corner
        history = VGroup()

        # ----------------------------------------------------------------
        # STEP 1: Consider the Equation
        # ----------------------------------------------------------------
        step1_text = Tex("Consider the differential equation in differential form:", font_size=40)
        step1_text.move_to(UP * 1.8)
        
        eq_orig = MathTex("M(x, y)dx + N(x, y)dy = 0")
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
        # STEP 2: The Exact Condition (Euler's Condition)
        # ----------------------------------------------------------------
        step2_text = Tex("The equation is \\textbf{exact} if the partial derivatives match:", font_size=40)
        step2_text.set_color_by_tex("exact", COLOR_HIGHLIGHT)
        step2_text.move_to(UP * 1.8)
        
        eq_condition = MathTex("\\frac{\\partial M}{\\partial y} = \\frac{\\partial N}{\\partial x}")
        eq_condition.set_color(COLOR_HIGHLIGHT)
        eq_condition.next_to(step2_text, DOWN, buff=0.4)
        
        self.play(Write(step2_text))
        self.play(FadeIn(eq_condition, shift=DOWN * 0.2))
        self.wait(2.5)

        # Move Step 2 to history
        hist_2 = eq_condition.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_2.next_to(hist_1, DOWN, buff=0.2).align_to(hist_1, LEFT)
        history.add(hist_2)

        self.play(FadeOut(step2_text), FadeOut(eq_condition), FadeIn(hist_2, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 3: Left side as a Total Differential
        # ----------------------------------------------------------------
        step3_text = Tex("This means the left side is a \\textbf{total differential} of $U(x,y)$:", font_size=40)
        step3_text.set_color_by_tex("total differential", COLOR_SUBST)
        step3_text.move_to(UP * 1.8)
        
        eq_differential = MathTex("dU = M(x, y)dx + N(x, y)dy = 0")
        eq_differential.set_color(COLOR_SUBST)
        eq_differential.next_to(step3_text, DOWN, buff=0.4)

        self.play(Write(step3_text))
        self.play(FadeIn(eq_differential, shift=DOWN * 0.2))
        self.wait(2.5)

        # Move Step 3 to history
        hist_3 = eq_differential.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_3.next_to(hist_2, DOWN, buff=0.2).align_to(hist_2, LEFT)
        history.add(hist_3)

        self.play(FadeOut(step3_text), FadeOut(eq_differential), FadeIn(hist_3, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 4: Properties of function U
        # ----------------------------------------------------------------
        step4_text = Tex("Where the function $U(x,y)$ satisfies relations:", font_size=40)
        step4_text.move_to(UP * 1.8)
        
        eq_relations = MathTex("\\frac{\\partial U}{\\partial x} = M(x, y) \\quad \\text{and} \\quad \\frac{\\partial U}{\\partial y} = N(x, y)")
        eq_relations.next_to(step4_text, DOWN, buff=0.4).scale(0.9)

        self.play(Write(step4_text))
        self.play(FadeIn(eq_relations, shift=DOWN * 0.2))
        self.wait(3.0)

        # Move Step 4 to history
        hist_4 = eq_relations.copy().scale(0.55).set_color(COLOR_HISTORY)
        hist_4.next_to(hist_3, DOWN, buff=0.2).align_to(hist_3, LEFT)
        history.add(hist_4)

        self.play(FadeOut(step4_text), FadeOut(eq_relations), FadeIn(hist_4, shift=UP * 0.2))

        # ----------------------------------------------------------------
        # STEP 5: Final Solution Form
        # ----------------------------------------------------------------
        conclusion_text = Tex("Integrating $dU = 0$ gives the implicit \\textbf{general solution}:", font_size=40)
        conclusion_text.set_color_by_tex("general solution", COLOR_RESULT)
        conclusion_text.move_to(DOWN * 0.8)
        
        eq_final = MathTex("U(x, y) = C")
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