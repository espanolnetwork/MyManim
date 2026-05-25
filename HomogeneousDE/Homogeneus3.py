%%manim -qm HomogeneousDEReducedForm

from manim import *

class HomogeneousDEReducedForm(Scene):
    def construct(self):
        # Color settings for clarity
        COLOR_EQ = GREEN
        COLOR_LAMBDA = YELLOW
        COLOR_TRANSFORM = ORANGE

        # Title for this part
        title = Text("Alternative Form & Substitution", font_size=35, color=BLUE)
        title.to_edge(UP)
        self.play(Write(title))
        self.wait(0.5)

        # Step 1: Present the general derivative form
        eq_form2_intro = Tex("Consider the equation written via derivative:", font_size=40)
        eq_form2_intro.move_to(UP * 1.5)
        
        eq_general = MathTex("y' = P(x, y)")
        eq_general.next_to(eq_form2_intro, DOWN, buff=1.5)
        
        self.play(Write(eq_form2_intro))
        self.play(FadeIn(eq_general, shift=DOWN * 0.2))
        self.wait(1.5)

        # Step 2: Replace intro text and transform equation to homogeneous form
        eq_form2_intro_2 = Tex("If $P(x,y)$ is homogeneous of degree $n=0$, it can be presented as:", font_size=40)
        eq_form2_intro_2.move_to(eq_form2_intro.get_center())
        
        eq_form2 = MathTex("y' = \\varphi\\left(\\frac{y}{x}\\right)")
        eq_form2.set_color(COLOR_EQ)
        eq_form2.move_to(eq_general.get_center())

        self.play(
            Transform(eq_form2_intro, eq_form2_intro_2),
            TransformMatchingShapes(eq_general, eq_form2)
        )
        self.wait(2)

        # Step 3: Highlight eq_form2 and show the substitution text
        substitution_box = SurroundingRectangle(eq_form2, color=COLOR_LAMBDA, buff=0.2)
        substitution_text = MathTex("y = u \\cdot x", color=COLOR_LAMBDA)
        substitution_text.next_to(substitution_box, RIGHT, buff=0.5)
        
        self.play(Create(substitution_box))
        self.play(Write(substitution_text))
        self.wait(1.5)

        # Step 4: Replace text again to explain the transformation to a separable equation
        eq_form2_intro_3 = Tex(
            r"This change of variable transforms the equation\\",
            r"into a \textbf{separable differential equation}",
            font_size=40
        )
        eq_form2_intro_3.set_color_by_tex("separable differential equation", COLOR_TRANSFORM)
        eq_form2_intro_3.move_to(eq_form2_intro.get_center())

        self.play(Transform(eq_form2_intro, eq_form2_intro_3))
        self.wait(3.5)

        # Smooth fade out to end the scene
        self.play(
            FadeOut(title),
            FadeOut(eq_form2_intro),
            FadeOut(eq_form2),
            FadeOut(substitution_box),
            FadeOut(substitution_text)
        )
        self.wait(1)

