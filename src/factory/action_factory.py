from __future__ import annotations

from xml.etree.ElementTree import Element

from src.actions.action import open_action, action, input_action, wait_action, click_action


class action_factory:

    @staticmethod
    def get_action(element: Element) -> action | None:
        action_type = element.find('type').text
        action_data = element.find('data').text.split(',')
        if action_type == 'open':
            return open_action(action_data[0])
        elif action_type == 'input':
            return input_action(action_data[0], action_data[1])
        elif action_type == 'click':
            return click_action(action_data[0])
        elif action_type == 'wait':
            return wait_action(int(action_data[0]))
        else:
            print('Unsupported action_type:', action_type)
