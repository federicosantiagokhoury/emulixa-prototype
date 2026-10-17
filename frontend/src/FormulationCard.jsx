function FormulationCard({ id, turbidity, viscosity }) {
    return (
        <div>
            <h2>Formulation #{id}</h2>
            <p>
                Turbidity: {turbidity === null ? "Not measured" : `${turbidity} NTU`}
            </p>
            <p>Viscosity: {viscosity}</p>
        </div>
    )
}

export default FormulationCard