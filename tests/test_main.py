import pytest
import main

def test_print_motd(capsys):
    main.print_motd()
    captured = capsys.readouterr()
    assert "Invalid day of week." not in captured.out

def test_display_menu(capsys):
    menu = {
        1: main.MenuItem("Test Item", 10.00),
    }
    main.display_menu(menu)
    captured = capsys.readouterr()
    assert "Test Item" in captured.out

def test_get_tip_percentage(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: '2')
    tip = main.get_tip_percentage()
    assert tip == 0.20
    monkeypatch.setattr('builtins.input', lambda _: '4')
    monkeypatch.setattr('builtins.input', lambda _: '20')
    tip = main.get_tip_percentage()
    assert tip == 0.20
    monkeypatch.setattr('builtins.input', lambda _: '5')
    tip = main.get_tip_percentage()
    assert tip == 0.0
