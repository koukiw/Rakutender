from schemas.event.show import Show, Rules
from models.event import Event
from fastapi import APIRouter, Depends


from utils.auth import auth_middle_ware

router = APIRouter()


@router.post('/event/show')
def show(condition: Rules, body: Show, isbool: bool = Depends(auth_middle_ware)):
    topNo = (body.page - 1) * 20
    if body.rules == None:
        event = Event.query.order_by(Event.start_at).limit(20).offset(topNo)
        return event
    
    execution = "event = Event.query.filter("
    if condition.startAt != None:
        execution = execution + "Event.start_at == " + str(condition.startAt) + ", "
    
    if condition.endAt != None:
        execution = execution + "Event.end_at == " + str(condition.endAt) + ", "

    if condition.limitUpper != None:
        execution = execution + "Event.limit <= " + str(condition.limitUpper) + ", "

    if condition.limitUnder != None:
        execution = execution + "Event.limit >= " + str(condition.limitUnder) + ", "

    if condition.categoryId != None:
        execution = execution + "Event.category_id == " + str(condition.categoryId) + ", "

    execution = execution[0:-2] + ").order_by(Event.start_at).limit(20).offset(topNo)"
    """
    (order: Order)
    if order.updown == True:
        if order.flag[0] == True:
            execution = execution + ".order_by(Event.start_at)"
        elif order.flag[1] == True:
            execution = execution + ".order_by(Event.limit)"
        elif order.flag[2] == True:
            execution = execution + ".order_by(Event.created_at)"
    else:
        if order.flag[0] == True:
            execution = execution + ".order_by(desc(Event.start_at))"
        elif order.flag[1] == True:
            execution = execution + ".order_by(desc(Event.limit))"
        elif order.flag[2] == True:
            execution = execution + ".order_by(desc(Event.created_at))"
    
    execution = execution + ".limit(20).offset(topNo)"

    """
    exec(execution)

    return event
