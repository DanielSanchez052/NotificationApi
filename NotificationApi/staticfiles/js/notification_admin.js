$(document).ready(()=>{
    $("#id_notification_type").on('select2:select',async (e) => {
        let notification_config_field = $('#id_config')
        let notification_types = await getNotificationType()
        let notification_type_id = e.params.data.id
        try {
            let notification_type = notification_types.find((type)=> type.id == notification_type_id)
            notification_config_field.val(JSON.stringify(notification_type.config))
            console.log(notification_config_field)
        } catch (error) {
            console.error(error)
            notification_config_field.val('')
        }
    })
})


async function getNotificationType(){
    try {
        let data = await fetch('http://localhost:8000/api/notifications/notification_type/')
        return (await data).json()
    } catch (error) {
        console.error(error)
    }
}

