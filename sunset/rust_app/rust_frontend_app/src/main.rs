mod config;
mod search;
mod ui;

use iced::Sandbox;
use ui::App;

fn main() -> iced::Result {
    App::run(iced::Settings::default())
}
