import streamlit as st
import pandas as pd


def main() -> None:
    df = pd.DataFrame(
        {
            "room": [
                "bedroom",
                "living room",
                "kitchen",
                "bedroom",
                "living room",
                "kitchen",
                "bedroom",
                "living room",
                "kitchen",
                "bedroom",
                "living room",
                "kitchen",
                "bedroom",
                "living room",
                "kitchen",
                "bedroom",
                "living room",
                "kitchen",
            ],
            "temperature": [
                7,
                8,
                12,
                8,
                9,
                13,
                5,
                6,
                12,
                10,
                12,
                15,
                14,
                14,
                16,
                18,
                19,
                17,
            ],
            "date": [
                "2024-12-30",
                "2024-12-30",
                "2024-12-30",
                "2025-01-01",
                "2025-01-01",
                "2025-01-01",
                "2025-01-02",
                "2025-01-02",
                "2025-01-02",
                "2025-01-03",
                "2025-01-03",
                "2025-01-03",
                "2025-01-04",
                "2025-01-04",
                "2025-01-04",
                "2025-01-05",
                "2025-01-05",
                "2025-01-05",
            ],
        }
    )
    df["date"] = pd.to_datetime(df["date"])
    df = df.set_index("date")

    st.dataframe(df)
    st.line_chart(df, y="temperature", color="room")


if __name__ == "__main__":
    main()
