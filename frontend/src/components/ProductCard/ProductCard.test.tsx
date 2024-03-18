import { ProductCard } from './ProductCard';
import { render } from '@testing-library/react';
import React from 'react';
import '@testing-library/jest-dom/extend-expect';

afterEach(jest.clearAllMocks);
it('Check ProductCard render correctly', () => {
    const rendered = render(
        <ProductCard
            name={'name'}
            description={'description'}
            category={'Электроника'}
            price={1000.0}
            priceSymbol={'$'}
            id={123}
            imgUrl={'qq'}
        />
    );

    expect(rendered.getByText('name')).toBeInTheDocument();
    expect(rendered.getByText('description')).toBeInTheDocument();
    expect(rendered.getByText('Электроника')).toBeInTheDocument();
    expect(rendered.getByText('1 000 $')).toBeInTheDocument();

    expect(rendered.asFragment()).toMatchSnapshot();
});

