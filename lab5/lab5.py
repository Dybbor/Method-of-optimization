from manimlib import *



def fibonacci(x): 
    if x <= 2 :
        return 1
    return fibonacci(x-1)+ fibonacci(x-2)

def func(x):
    return (x**3) /3  - (x**2) /2 - x -1
    # return (x-2)**2 +1
class Test(Scene):


    def CreatePoint(self, axes, x, y, myColor):
        dot = SmallDot(color = myColor)
        dot.move_to(axes.c2p(x,y))
        return dot        

    def construct(self):
        
        axes = Axes(
            x_range=( -1,4, 1),
            y_range=(-5, 6, 1 ),
            height=6,
            width=3,
            axis_config={
                "stroke_color": GREY_A,
                "stroke_width": 1,
            },
        )
        axes.add_coordinate_labels(
            font = "Consolas",
            font_size=24,
            num_decimal_places=0,
        )
        fun_graph = axes.get_graph(
            lambda x: (x**3) /3  - (x**2) /2 - x -1 ,
            # lambda x:  (x-2)**2 +1,
            color=BLUE,           
        )
      
        label = Tex("(x-2)^2 +1", font_size = 24)
        label_graph = axes.get_graph_label(fun_graph, label, x = 3.7, buff=-2)
        self.play(Write(axes, run_time = 2))
        self.play(
            ShowCreation(fun_graph),
            FadeIn(label_graph, RIGHT)
            )
       
        gr = VGroup(axes, fun_graph, label_graph)
        self.play(gr.animate.scale(1.8), run_time = 1)

        a = 0 
        b = 3
        n = 12
        eps = 0.00000000000000001
        sigma = 0.01

        template_x = Tex("x1 = b - (b-a)*\\frac{F_{n-k-1}} {F_{n-k}}\t", font_size = 20)
        template_y = Tex("x2 = a + (b-a)*\\frac{F_{n-k-1}} {F_{n-k}}\t", font_size = 20)
        gr_eq = VGroup(template_x, template_y).arrange(DOWN)
        gr_eq.to_corner(RIGHT)
        self.play(Write(gr_eq))

        dotx = self.CreatePoint(axes,2,2, YELLOW)
        doty = self.CreatePoint(axes,1,1,RED)

        count = 0

        while((b-a)/fibonacci(count)>sigma):
            count +=1
            print("count ",count) # count iteration fibonacci method

        new_v_line_a = 0
        new_v_line_b = 0
        border_graph = 0
        underline_graph = 0 
        right_graph = 0
        v_line_a = 0
        v_line_b = 0
        text = 0
        x = 0
        y = 0
        k = 0
        for i in range (0, n - 2):
            template = 0

            x = b - (b-a)*fibonacci(n - k - 1 )/ fibonacci(n - k)
            y = a + (b-a)*fibonacci(n - k - 1 )/ fibonacci(n - k)
            if (i == 0):
                v_line_a = axes.get_v_line_to_graph(a, fun_graph, color = ORANGE)
                v_line_b = axes.get_v_line_to_graph(b, fun_graph, color = ORANGE)
                border_graph = axes.get_graph(
                    lambda x:  0,
                    color = ORANGE,    
                    x_range = (a,b)   
                )
                self.play(
                        ShowCreation(v_line_a),
                        ShowCreation(v_line_b),
                        ShowCreation(border_graph)
                        )
       
            dotx = SmallDot(color = YELLOW)
            doty = SmallDot(color = RED)
            dotx.move_to(axes.c2p(x,func(x)))
            doty.move_to(axes.c2p(y,func(y)))
            self.play(
                FadeIn(dotx, DOWN),
                FadeIn(doty, DOWN)
            )
            v_line_x = axes.get_v_line(dotx.get_bottom())
            h_line_x = axes.get_h_line(dotx.get_left())
            v_line_y = axes.get_v_line(doty.get_bottom())
            h_line_y = axes.get_h_line(doty.get_left())
            self.play(
                ShowCreation(v_line_x),
                ShowCreation(h_line_x),
                ShowCreation(v_line_y),
                ShowCreation(h_line_y),
            )
            template1 = "x1: " + str(round(x,4)) + " y1: " + str(round(func(x),4))
            template2 = "x2: " + str(round(y,4)) + " y2: " + str(round(func(y),4))
            template3 = "f(x) < f(y)" if (func(x) < func(y)) else "f(x) > f(y)"
            template4 = "i: " + str(i)
            text = Text(template4 + "\n" +template1 + "\n" + template2 + "\n" +template3, font_size = 20)
            text.to_corner(DOWN)
            self.play(FadeIn(text))
            self.wait(2)
            print(i)
            k += 1
            print(f"{a,b}")
            print(f" x = {x} ,  y = {y}")
            qx, qy = func(x), func(y)
            print(f"fx = {qx} , fy = {qy}\n")
            print(fibonacci(n-k-1), fibonacci(n-k))
            if (qx < qy):
                b = y
                y = x               
                underline_graph = axes.get_graph(
                    lambda x: 0,
                    x_range = (a,b),
                    color = WHITE
                )  
                right_graph = axes.get_graph(
                    lambda x: 0,
                    x_range = (a, b),
                    color = ORANGE
                ) 

                self.play(
                    ShowCreation(underline_graph)
                )
                new_v_line_b = axes.get_v_line_to_graph(b, fun_graph, color = ORANGE) 
                self.play(
                    FadeOut(underline_graph),
                    ReplacementTransform(v_line_b, new_v_line_b),
                    ReplacementTransform(border_graph, right_graph),
                    FadeOut(dotx),
                    FadeOut(doty),
                    FadeOut(v_line_x),
                    FadeOut(v_line_y),
                    FadeOut(h_line_x),
                    FadeOut(h_line_y),
                    FadeOut(text)
                )
                v_line_b = axes.get_v_line_to_graph(b, fun_graph, color = ORANGE)
                border_graph = axes.get_graph(
                    lambda x:  0,
                    color = ORANGE,    
                    x_range = (a,b)   
                )              
                self.play(
                    FadeIn(border_graph),
                    FadeOut(right_graph),
                    FadeIn(v_line_b),
                    FadeOut(new_v_line_b)  
                )
            else:
                a = x
                x = y
                underline_graph = axes.get_graph(
                    lambda x: 0,
                    x_range = (a,b),
                    color = WHITE
                ) 
                right_graph = axes.get_graph(
                    lambda x: 0,
                    x_range = (a,b),
                    color = ORANGE
                ) 
                self.play(
                    ShowCreation(underline_graph)
                )
                new_v_line_a = axes.get_v_line_to_graph(a, fun_graph, color = ORANGE) 
                self.play(
                    FadeOut(underline_graph),
                    ReplacementTransform(v_line_a, new_v_line_a),
                    ReplacementTransform(border_graph, right_graph),
                    FadeOut(dotx),
                    FadeOut(doty),
                    FadeOut(v_line_x),
                    FadeOut(v_line_y),
                    FadeOut(h_line_x),
                    FadeOut(h_line_y),
                    FadeOut(text)
                )
                v_line_a = axes.get_v_line_to_graph(a, fun_graph, color = ORANGE)
                border_graph = axes.get_graph(
                    lambda x:  0,
                    color = ORANGE,    
                    x_range = (a,b)   
                ) 
                self.play(
                    FadeIn(v_line_a),
                    FadeOut(new_v_line_a),
                    FadeIn(border_graph),
                    FadeOut(right_graph)
                )

        print(f"min point = ({round(x)}, {round(func(x))})")
        self.play(
            FadeOut(border_graph),
            FadeOut(v_line_a),
            FadeOut(v_line_b)
        )
        min_dot = SmallDot(color = YELLOW)
        dotx.move_to(axes.c2p(x,func(x)))
        self.play(
             FadeIn(dotx, DOWN)
        )
        template = "min (" + str(round(x, 6)) + "," + str(round(func(x),6)) + ")" 
        text = Text(template + "       \n" +"    \n", font_size = 20)
        text.to_corner(DOWN)
        self.play(FadeIn(text))