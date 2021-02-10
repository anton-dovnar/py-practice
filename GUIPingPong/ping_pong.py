from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.properties import (
    NumericProperty,
    ObjectProperty,
    ReferenceListProperty,
)
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.widget import Widget
from kivy.vector import Vector


class PongPaddle(Widget):
    score = NumericProperty(0)

    def bounce_ball(self, ball):
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            offset = (ball.center_y - self.center_y) / (self.height / 2)
            bounced = Vector(-1 * vx, vy)
            vel = bounced * 1.1
            ball.velocity = vel.x, vel.y + offset


class PongBall(Widget):
    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        self.pos = Vector(*self.velocity) + self.pos


class PongGame(Widget):
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    player2 = ObjectProperty(None)

    def serve_ball(self, vel=(4, 0)):
        self.ball.center = self.center
        self.ball.velocity = vel

    def restart(self, *args):
        self.player1.score = 0
        self.player2.score = 0
        self.result.dismiss()
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def exit(self, *args, **kwargs):
        App.get_running_app().stop()
        Window.close()

    def display_winner(self, player):
        Clock.unschedule(self.update)

        # TODO Fix restart button

        box = BoxLayout(orientation='vertical', padding=10)
        box.add_widget(
            Label(
                text=f'Winner Player {player} \n'
                f'Score: {self.player1.score} - {self.player2.score}',
                font_size=20,
                valign='center',
                halign='center'
            )
        )
        box.add_widget(
            Button(
                text='Restart',
                size_hint=(1, .2),
                font_size=20,
                on_press=self.restart
            )
        )
        box.add_widget(
            Button(
                text='Exit',
                size_hint=(1, .2),
                font_size=20,
                on_press=self.exit
            )
        )

        popup_window = Popup(
            title='Game Over', title_size=30,
            title_align='center', content=box,
            auto_dismiss=False
        )
        self.result = popup_window
        popup_window.open()

    def update(self, dt):
        self.ball.move()

        self.player1.bounce_ball(self.ball)
        self.player2.bounce_ball(self.ball)

        if (self.ball.y < self.y) or (self.ball.top > self.top):
            self.ball.velocity_y *= -1

        if self.ball.x < self.x:
            self.player2.score += 1

            if self.player2.score == 10:
                self.display_winner(2)
            else:
                self.serve_ball(vel=(4, 0))

        if self.ball.x > self.width:
            self.player1.score += 1

            if self.player1.score == 10:
                self.display_winner(1)
            else:
                self.serve_ball(vel=(4, 0))

    def on_touch_move(self, touch):
        if touch.x < self.width / 2 - 15:
            if touch.y > (height := self.height - self.player2.height / 2):
                self.player1.center_y = height
            elif touch.y < (height := self.player2.height / 2):
                self.player1.center_y = height
            else:
                self.player1.center_y = touch.y

        if touch.x > self.width - self.width / 2 + 15:
            if touch.y > (height := self.height - self.player2.height / 2):
                self.player2.center_y = height
            elif touch.y < (height := self.player2.height / 2):
                self.player2.center_y = height
            else:
                self.player2.center_y = touch.y


class PongApp(App):
    def build(self):
        game = PongGame()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    PongApp().run()
