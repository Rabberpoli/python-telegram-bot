#!/usr/bin/env python
# -*- coding: utf-8 -*-
# A library that provides a Python interface to the Telegram Bot API
# Copyright (C) 2015-2018
# Leandro Toledo de Souza <devs@python-telegram-bot.org>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser Public License for more details.
#
# You should have received a copy of the GNU Lesser Public License
# along with this program.  If not, see [http://www.gnu.org/licenses/].

import pytest

from telegram import Poll, PollOption


@pytest.fixture(scope='class')
def poll(bot):
    return Poll(TestPoll.id,
                TestPoll.question,
                TestPoll.options,
                TestPoll.is_closed)


class TestPoll(object):
    id = 'id'
    question = 'Test?'
    options = [PollOption('test', 10), PollOption('test2', 11)]
    is_closed = True

    def test_de_json(self, bot):
        json_dict = {
            'id': TestPoll.id,
            'question': TestPoll.question,
            'options': [o.to_dict() for o in TestPoll.options],
            'is_closed': TestPoll.is_closed
        }
        poll = Poll.de_json(json_dict, bot)

        assert poll.id == self.id
        assert poll.question == self.question
        assert poll.options == self.options
        assert poll.options[0].text == self.options[0].text
        assert poll.options[0].voter_count == self.options[0].voter_count
        assert poll.options[1].text == self.options[1].text
        assert poll.options[1].voter_count == self.options[1].voter_count
        assert poll.is_closed == self.is_closed

    def test_to_dict(self, poll):
        poll_dict = poll.to_dict()

        assert isinstance(poll_dict, dict)
        assert poll_dict['id'] == poll.id
        assert poll_dict['question'] == poll.question
        assert poll_dict['options'] == [o.to_dict() for o in poll.options]
        assert poll_dict['is_closed'] == poll.is_closed
