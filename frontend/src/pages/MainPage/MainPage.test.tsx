import { render, screen, fireEvent } from '@testing-library/react';
import { createRoot } from 'react-dom/client';
import { MainPage } from './MainPage';
import { act } from 'react-dom/test-utils';
import '@testing-library/jest-dom';

jest.mock('../../hooks', () => ({
  ...jest.requireActual('../../hooks'), // Импортируем все остальные хуки как обычно
  useCurrentTime: () => '12:00 PM',
}));

describe('MainPage', () => {
  it('renders without mistakes', () => {
    act(() => {
      render(<MainPage />);
    });
  });

  it('shows current time', () => {
    render(<MainPage />);
    expect(screen.getByText('12:00 PM')).toBeInTheDocument();
  });

  it('shows categories', () => {
    const { container, getByText } = render(<MainPage />);
    const categoryButton = container.querySelector('.categories__badge');
    expect(categoryButton).not.toBeNull();
  });

  it('adds category on click', () => {
    const { container, getByText } = render(<MainPage />);
    const categoryButton = screen.getByText('Электроника', {selector: '.categories__badge'});
    expect(categoryButton).not.toBeNull();

    if (categoryButton) fireEvent.click(categoryButton);
    const excludedProduct = screen.queryByText('Костюм гуся');
    expect(excludedProduct).toBeNull();
  });
});
