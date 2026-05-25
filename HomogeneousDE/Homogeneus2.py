%%manim -qm HomogeneousDEPart

from manim import *

class HomogeneousDEPart(Scene):
    def construct(self):
        # Color settings for clarity
        COLOR_DEGREE = ORANGE
        COLOR_BOX_M = YELLOW
        COLOR_BOX_N = PINK

        # ----------------------------------------------------------------
        # PART 2: Homogeneous Differential Equation
        # ----------------------------------------------------------------
        title_2 = Text("Homogeneous Differential Equation", font_size=35, color=BLUE)
        title_2.to_edge(UP)
        self.play(Write(title_2))
        self.wait(0.5)

        # Form 1: M dx + N dy = 0 (using separated strings for precise sub-element selection)
        eq_form1 = MathTex("M(x, y)", "dx + ", "N(x, y)", "dy = 0")
        eq_form1.move_to(UP * 1.5)
        self.play(FadeIn(eq_form1, shift=UP * 0.2))
        self.wait(1)

        # Condition text
        condition_text = Tex(
            r"$M(x,y)$ and $N(x,y)$ are homogeneous functions \\ of the exact same degree $n$:",
            font_size=40, color=COLOR_DEGREE
        )
        condition_text.next_to(eq_form1, DOWN, buff=0.4)
        self.play(Write(condition_text))
        self.wait(0.5)

        # Boxes to highlight M and N in the main equation
        box_M = SurroundingRectangle(eq_form1[0], color=COLOR_BOX_M, buff=0.1)
        box_N = SurroundingRectangle(eq_form1[2], color=COLOR_BOX_N, buff=0.1)

        # Definition formula for M(x, y)
        def_M = MathTex("M(\\lambda x, \\lambda y) = \\lambda^n M(x, y)")
        def_M.set_color(COLOR_BOX_M)
        def_M.next_to(condition_text, DOWN, buff=0.5).shift(LEFT * 2.2)

        # Definition formula for N(x, y)
        def_N = MathTex("N(\\lambda x, \\lambda y) = \\lambda^n N(x, y)")
        def_N.set_color(COLOR_BOX_N)
        def_N.next_to(def_M, DOWN, buff=0.5).shift(RIGHT * 2.2)

        # Animate M highlight and its definition equation
        self.play(Create(box_M))
        self.play(Write(def_M))
        self.wait(0.5)

        # Animate N highlight and its definition equation
        self.play(Create(box_N))
        self.play(Write(def_N))
        self.wait(2.5)

        # Smooth fade out to end the scene beautifully
        self.play(
            FadeOut(title_2),
            FadeOut(eq_form1),
            FadeOut(condition_text),
            FadeOut(box_M),
            FadeOut(box_N),
            FadeOut(def_M),
            FadeOut(def_N)
        )
        self.wait(1)