class TitleMixin:
    def get_title(self):
        return "Mixin Title"

class ContentMixin:
    def get_content(self):
        return "Mixin Content"

class AuthorMixin:
    def get_author(self):
        return "Mixin Author"

class DateMixin:
    def get_date(self):
        return "Mixin Date"

class SummaryMixin:
    def get_summary(self):
        return "Mixin Summary"

class TagMixin:
    def get_tags(self):
        return ["tag1", "tag2"]

class CategoryMixin:
    def get_category(self):
        return "Mixin Category"

class StatusMixin:
    def get_status(self):
        return "Mixin Status"

class CommentMixin:
    def get_comments(self):
        return ["Comment 1", "Comment 2"]

class RatingMixin:
    def get_rating(self):
        return 5
