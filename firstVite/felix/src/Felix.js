import React, { useState } from 'react';

export default function Felix() {
    const [pugCount, setPugCount] = useState(1);

    const randomEffect = () => {
        const effects = [
            { transform: 'scale(1.1)', filter: 'brightness(120%)' },
            { transform: 'rotate(5deg)', filter: 'sepia(70%)' },
            { filter: 'grayscale(100%)' },
            { transform: 'rotate(-5deg)', boxShadow: '5px 5px 10px rgba(0,0,0,0.2)' },
            { transform: 'scaleX(-1)' },  // Horizontal flip
            { transform: 'scaleY(-1)' }   // Vertical flip
        ];
        return effects[Math.floor(Math.random() * effects.length)];
    };

    const dupeImage = () => {
        setPugCount(prevCount => prevCount + 1);
    };

    return (
        <div className="Felix">
            <button onClick={dupeImage}>press! button</button>
            <div>
                {Array.from({ length: pugCount }).map((_, index) => (
                    <img
                        key={index}
                        style={randomEffect()}
                        src={process.env.PUBLIC_URL + '/felix.jpg'}
                        alt='pug'
                    />
                ))}
            </div>
        </div>
    );
}
