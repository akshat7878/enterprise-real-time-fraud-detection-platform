"""Structural checks only; does not substitute for visual review in PowerPoint."""
from pathlib import Path
from pptx import Presentation

path = Path(__file__).with_name('Enterprise_Fraud_Detection_Platform.pptx')
deck = Presentation(path)
assert len(deck.slides) == 13, f'Expected 13 slides; got {len(deck.slides)}'
for number, slide in enumerate(deck.slides, 1):
    assert slide.notes_slide.notes_text_frame.text.strip(), f'Missing notes: {number}'
    assert any(s.has_text_frame and s.text.strip() for s in slide.shapes)
    for shape in slide.shapes:
        assert shape.left >= 0 and shape.top >= 0, f'Negative position: {number}'
        assert shape.left + shape.width <= deck.slide_width, f'Outside slide width: {number}'
        assert shape.top + shape.height <= deck.slide_height, f'Outside slide height: {number}'
print('PASS: 13 slides, speaker notes, text, and all shapes inside slide bounds.')
