import uvicorn
from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app.db.database import engine, Base
from app.users.routes import user_router, player_router, admin_router, admin_type_router
from app.questions.routes import category_router, question_router
from app.quizzes.routes import quiz_router, q_and_a_router

Base.metadata.create_all(bind=engine)


def init_app():

    app = FastAPI()
    app.include_router(user_router)
    app.include_router(player_router)
    app.include_router(admin_router)
    app.include_router(admin_type_router)
    app.include_router(category_router)
    app.include_router(question_router)
    app.include_router(quiz_router)
    app.include_router(q_and_a_router)

    return app


app = init_app()


@app.get("/", include_in_schema=False)
def hello_world():
    return RedirectResponse('/docs')


if __name__ == '__main__':

    uvicorn.run(app)
