from django.test import TestCase
from app import models


class TestComputer(TestCase):
    def test_can_create_computer(self):
        computer = models.create_computer(
            "Janets Desktop",
            "AB:AB:AB:AB:AB:10",
            1234567890,
            "Office 1",
        )
        print(computer)
        self.assertEqual(computer.id, 1)
        self.assertEqual(computer.name, "Janets Desktop")
        self.assertEqual(computer.mac, "AB:AB:AB:AB:AB:10")
        self.assertEqual(computer.model_num, 1234567890)
        self.assertEqual(computer.location, "Office 1")

    def test_can_view_all_computers_at_once(self):
        computers_data = [
            {
                "name": "Elias comp",
                "mac": "AC:AD:AC:BF:10:15",
                "model_num": 1987654321,
                "location": "Office 2",
            },
            {
                "name": "Martin comp",
                "mac": "Ad:AD:Af:BF:12:11",
                "model_num": 1987654321,
                "location": "Office 2",
            },
            {
                "name": "Alma comp",
                "mac": "AC:AE:AF:BF:10:15",
                "model_num": 1987654321,
                "location": "Office 2",
            },
        ]

        for computer_data in computers_data:
            models.create_computer(
                computer_data["name"],
                computer_data["mac"],
                computer_data["model_num"],
                computer_data["location"],
            )

        computers = models.all_computers()

        self.assertEqual(len(computers), len(computers_data))

        computers_data = sorted(computers_data, key=lambda c: c["name"])
        computers = sorted(computers, key=lambda c: c.name)

        for data, computer in zip(computers_data, computers):
            self.assertEqual(data["name"], computer.name)
            self.assertEqual(data["mac"], computer.mac)
            self.assertEqual(data["model_num"], computer.model_num)
            self.assertEqual(data["location"], computer.location)

    def test_can_search_by_mac(self):
        computers_data = [
            {
                "name": "Elias comp",
                "mac": "AC:AD:AC:BF:10:15",
                "model_num": 1987654321,
                "location": "Office 2",
            },
            {
                "name": "Martin comp",
                "mac": "Ad:AD:Af:BF:12:11",
                "model_num": 1987654321,
                "location": "Office 2",
            },
            {
                "name": "Alma comp",
                "mac": "AC:AE:AF:BF:10:15",
                "model_num": 1987654321,
                "location": "Office 2",
            },
        ]

        for computer_data in computers_data:
            models.create_computer(
                computer_data["name"],
                computer_data["mac"],
                computer_data["model_num"],
                computer_data["location"],
            )

        self.assertIsNone(models.find_computer_by_mac("aousnth"))

        computer = models.find_computer_by_mac("AC:AE:AF:BF:10:15")

        self.assertIsNotNone(computer)
        self.assertEqual(computer.mac, "AC:AE:AF:BF:10:15")

    def test_can_view_in_location(self):
        computers_data = [
            {
                "name": "Elias comp",
                "mac": "AC:AD:AC:BF:10:15",
                "model_num": 1987654321,
                "location": "Office 1",
            },
            {
                "name": "Martin comp",
                "mac": "Ad:AD:Af:BF:12:11",
                "model_num": 1987654321,
                "location": "Office 2",
            },
            {
                "name": "Alma comp",
                "mac": "AC:AE:AF:BF:10:15",
                "model_num": 1987654321,
                "location": "Office 2",
            },
        ]

        for computer_data in computers_data:
            models.create_computer(
                computer_data["name"],
                computer_data["mac"],
                computer_data["model_num"],
                computer_data["location"],
            )

        self.assertEqual(len(models.computers_in_location("Office 2")), 2)

    def test_can_update_computers_mac(self):
        computers_data = [
            {
                "name": "Elias comp",
                "mac": "AC:AD:AC:BF:10:15",
                "model_num": 1987654321,
                "location": "Office 2",
            },
            {
                "name": "Martin comp",
                "mac": "Ad:AD:Af:BF:12:11",
                "model_num": 1987654321,
                "location": "Office 2",
            },
            {
                "name": "Alma comp",
                "mac": "AC:AE:AF:BF:10:15",
                "model_num": 1987654321,
                "location": "Office 2",
            },
        ]

        for computer_data in computers_data:
            models.create_computer(
                computer_data["name"],
                computer_data["mac"],
                computer_data["model_num"],
                computer_data["location"],
            )

        models.update_computer_location("AC:AD:AC:BF:10:15", "Office 1")

        self.assertEqual(
            models.find_computer_by_mac("AC:AD:AC:BF:10:15").mac, "AC:AD:AC:BF:10:15"
        )

    def test_can_delete_computer(self):
        computers_data = [
            {
                "name": "Elias comp",
                "mac": "AC:AD:AC:BF:10:15",
                "model_num": 1987654321,
                "location": "Office 2",
            },
            {
                "name": "Martin comp",
                "mac": "Ad:AD:Af:BF:12:11",
                "model_num": 1987654321,
                "location": "Office 2",
            },
            {
                "name": "Alma comp",
                "mac": "AC:AE:AF:BF:10:15",
                "model_num": 1987654321,
                "location": "Office 2",
            },
        ]

        for computer_data in computers_data:
            models.create_computer(
                computer_data["name"],
                computer_data["mac"],
                computer_data["model_num"],
                computer_data["location"],
            )

        models.delete_computer("Ad:AD:Af:BF:12:11")

        self.assertEqual(len(models.all_computers()), 2)
