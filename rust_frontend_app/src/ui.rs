use iced::{widget::{Column, Row, Text, TextInput, Button, Scrollable}, Alignment, Element, Sandbox, Settings, Command, Length};
use crate::config::AppConfig;
use crate::search::{SearchRequest, SearchResult};

#[derive(Debug, Clone)]
pub enum Message {
    QueryChanged(String),
    SubmitQuery,
    QueryResult(Result<Vec<SearchResult>, String>),
    BackendUrlChanged(String),
    GroupIdChanged(String),
    SaveSettings,
    ClearQuery,
}

pub struct App {
    pub config: AppConfig,
    pub query: String,
    pub results: Vec<SearchResult>,
    pub loading: bool,
    pub error: Option<String>,
}

impl Default for App {
    fn default() -> Self {
        Self {
            config: AppConfig::load(),
            query: String::new(),
            results: Vec::new(),
            loading: false,
            error: None,
        }
    }
}

impl Sandbox for App {
    type Message = Message;

    fn new() -> Self {
        App::default()
    }

    fn title(&self) -> String {
        "Graphiti Rust Frontend".into()
    }

    fn update(&mut self, message: Message) {
        match message {
            Message::QueryChanged(q) => self.query = q,
            Message::ClearQuery => {
                self.query.clear();
                self.results.clear();
                self.error = None;
            },
            Message::SubmitQuery => {
                self.loading = true;
                // In MVP: trigger async search here (future: iced futures)
            },
            Message::QueryResult(res) => {
                self.loading = false;
                match res {
                    Ok(results) => self.results = results,
                    Err(e) => self.error = Some(e),
                }
            },
            Message::BackendUrlChanged(url) => self.config.backend_url = url,
            Message::GroupIdChanged(gid) => self.config.group_id = gid,
            Message::SaveSettings => self.config.save(),
        }
    }

    fn view(&self) -> Element<Message> {
        let input = TextInput::new("Search...", &self.query)
            .on_input(Message::QueryChanged)
            .on_submit(Message::SubmitQuery)
            .padding(10)
            .size(20);
        let submit = Button::new(Text::new("Search")).on_press(Message::SubmitQuery);
        let clear = Button::new(Text::new("Clear")).on_press(Message::ClearQuery);
        let error = if let Some(err) = &self.error {
            Text::new(err).style(iced::theme::Text::Color([1.0, 0.0, 0.0, 1.0].into())).size(16)
        } else {
            Text::new("")
        };
        let results_vec = self.results.iter().map(|r| {
            Row::new()
                .push(Text::new(&r.title).size(20))
                .push(Text::new(&r.summary).size(16))
                .into()
        }).collect::<Vec<_>>();
        let results = Scrollable::new(
            Column::with_children(results_vec)
        ).height(Length::FillPortion(2));
        Column::new()
            .align_items(Alignment::Center)
            .push(input)
            .push(Row::new().push(submit).push(clear))
            .push(error)
            .push(results)
            .into()
    }
}
