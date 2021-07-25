from manim import *
import numpy as np 

class Primer_video(Scene):
    def construct(self):
        texto0 = Text("¡¡Hola Mundo!! Este es mi primer video en Manim :D", size=0.5)
        self.play(Write(texto0))
        self.play(FadeOut(texto0))

        texto1 = Text("Veremos el sesgo del estimador de OLS", slant=ITALIC,size=0.5)
        texto2 = Text("Mostraremos matricialmente el modelo estimado, el modelo real y el término del sesgo", t2s={'world':ITALIC}, size=0.5)
        grupo1 = VGroup(texto1,texto2).arrange(DOWN)
        self.play(Write(grupo1))
        self.play(FadeOut(grupo1))
        

        m_estimado = Tex(r"$Y=X_{1}\beta_{1}+u \Rightarrow$ Modelo Estimado")
        m_real = Tex("$Y=X_{1}\\beta_{1}+X_{2}\\beta_{2}+u \\Rightarrow$ Modelo Real")       
        E_estimador = MathTex(r"E[\hat{\beta}_{1}]=\beta_{1}+", r"\frac{cov(X_{1},X_{2})}{Var(X_{1})}\beta_{2}")
        sesgo = SurroundingRectangle(E_estimador[1], buff=.1)
        E_estimador[1].set_color(RED)

        grupo2 = VGroup(m_estimado,m_real).arrange(DOWN)
        self.play(Write(grupo2), run_time=2)
        self.play(FadeOut(grupo2))
        
        self.play(Write(E_estimador))
        self.play(Create(sesgo))

        bracket = Brace(sesgo)
        bracket_texto = bracket.get_text("Sesgo")
        self.play(GrowFromCenter(bracket), FadeIn(bracket_texto), run_time=2)
        self.wait(3)
