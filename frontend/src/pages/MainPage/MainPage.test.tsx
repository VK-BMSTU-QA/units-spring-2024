jest.mock('../../hooks/useCurrentTime', () => ({
    useCurrentTime: () => '',
}));

import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { MainPage } from './MainPage';
import React from 'react';

afterEach(jest.clearAllMocks);
describe('Product card test', () => {
    it('should render correctly', () => {
        const rendered = render(<MainPage />);

        expect(rendered.asFragment()).toMatchSnapshot();
    });
});
