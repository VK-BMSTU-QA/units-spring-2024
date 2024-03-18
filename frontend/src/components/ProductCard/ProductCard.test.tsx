import React from 'react';
import { render } from '@testing-library/react';
import '@testing-library/jest-dom';
import { ProductCard } from './ProductCard';

afterEach(jest.clearAllMocks);
describe('Product card test', () => {
    it('should render correctly', () => {
        const rendered = render(
            <ProductCard
                name="name"
                description={'desc'}
                category={'Одежда'}
                price={123}
                id={1}
                imgUrl={'qwwe'}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
    });

    test('does not render image if imgUrl is not provided', () => {
        const rendered = render(
            <ProductCard
                name="name"
                description={'desc'}
                category={'Одежда'}
                price={123}
                id={1}
                imgUrl={''}
            />
        );

        expect(rendered.asFragment()).toMatchSnapshot();
    });
});
