import logging

from ..orm import SqlAlchemy
from ..views import IssueViewBuilder, IssueListBuilder
from {{cookiecutter.app_name}}.services import ReportIssueHandler, TriageIssueHandler, IssueAssignedHandler, AssignIssueHandler

from .emails import LoggingEmailSender

import {{cookiecutter.app_name}}.domain.messages as msg
from {{cookiecutter.app_name}}.domain.ports import MessageBus

db = SqlAlchemy('sqlite:///{{cookiecutter.app_name}}.db')
db.configure_mappings()
db.create_schema()

bus = MessageBus()
db.associate_message_bus(bus)

issue_view_builder = IssueViewBuilder(db)
issue_list_builder = IssueListBuilder(db)

report_issue = ReportIssueHandler(db.unit_of_work_manager)
assign_issue = AssignIssueHandler(db.unit_of_work_manager)
triage_issue = TriageIssueHandler(db.unit_of_work_manager)
issue_assigned = IssueAssignedHandler(issue_view_builder, LoggingEmailSender())

bus.subscribe_to(msg.ReportIssueCommand, report_issue)
bus.subscribe_to(msg.TriageIssueCommand, triage_issue)
bus.subscribe_to(msg.IssueAssignedToEngineer, issue_assigned)
bus.subscribe_to(msg.AssignIssueCommand, assign_issue)
