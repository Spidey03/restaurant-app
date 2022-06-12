export default function Notification({response}){
    return (
        <div class_name="notification__container">
            <h1 className="notification__header">{response['res_status']}</h1>
            <p className="notification__desc">{response['response']}</p>
        </div>
    )
}