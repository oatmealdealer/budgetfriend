# generated by datamodel-codegen:
#   filename:  ynab_schema.json
#   timestamp: 2021-08-17T00:24:34+00:00

from __future__ import annotations

from datetime import date, datetime
from enum import Enum
from typing import Any, List, Optional
from uuid import UUID

from pydantic import BaseModel, Field, constr


class Model(BaseModel):
    __root__: Any


class ErrorDetail(BaseModel):
    id: str
    name: str
    detail: str


class User(BaseModel):
    id: UUID


class DateFormat(BaseModel):
    format: str


class CurrencyFormat(BaseModel):
    iso_code: str
    example_format: str
    decimal_digits: int
    decimal_separator: str
    symbol_first: bool
    group_separator: str
    currency_symbol: str
    display_symbol: bool


class BudgetSettings(BaseModel):
    date_format: DateFormat
    currency_format: CurrencyFormat


class Type(Enum):
    checking = "checking"
    savings = "savings"
    cash = "cash"
    creditCard = "creditCard"
    lineOfCredit = "lineOfCredit"
    otherAsset = "otherAsset"
    otherLiability = "otherLiability"
    payPal = "payPal"
    merchantAccount = "merchantAccount"
    investmentAccount = "investmentAccount"
    mortgage = "mortgage"


class Account(BaseModel):
    id: UUID
    name: str
    type: Type = Field(
        ...,
        description="The type of account. Note: payPal, merchantAccount, investmentAccount, and mortgage types have been deprecated and will be removed in the future.",
    )
    on_budget: bool = Field(..., description="Whether this account is on budget or not")
    closed: bool = Field(..., description="Whether this account is closed or not")
    note: Optional[str] = None
    balance: int = Field(..., description="The current balance of the account in milliunits format")
    cleared_balance: int = Field(
        ...,
        description="The current cleared balance of the account in milliunits format",
    )
    uncleared_balance: int = Field(
        ...,
        description="The current uncleared balance of the account in milliunits format",
    )
    transfer_payee_id: UUID = Field(
        ...,
        description="The payee id which should be used when transferring to this account",
    )
    direct_import_linked: Optional[bool] = Field(
        None,
        description="Whether or not the account is linked to a financial institution for automatic transaction import.",
    )
    direct_import_in_error: Optional[bool] = Field(
        None,
        description="If an account linked to a financial institution (direct_import_linked=true) and the linked connection is not in a healthy state, this will be true.",
    )
    deleted: bool = Field(
        ...,
        description="Whether or not the account has been deleted.  Deleted accounts will only be included in delta requests.",
    )


class Type1(Enum):
    checking = "checking"
    savings = "savings"
    creditCard = "creditCard"
    cash = "cash"
    lineOfCredit = "lineOfCredit"
    otherAsset = "otherAsset"
    otherLiability = "otherLiability"


class SaveAccount(BaseModel):
    name: str = Field(..., description="The name of the account")
    type: Type1 = Field(..., description="The account type")
    balance: int = Field(..., description="The current balance of the account in milliunits format")


class CategoryGroup(BaseModel):
    id: UUID
    name: str
    hidden: bool = Field(..., description="Whether or not the category group is hidden")
    deleted: bool = Field(
        ...,
        description="Whether or not the category group has been deleted.  Deleted category groups will only be included in delta requests.",
    )


class GoalTypeEnum(Enum):
    TB = "TB"
    TBD = "TBD"
    MF = "MF"
    NEED = "NEED"


class GoalType(BaseModel):
    __root__: Optional[GoalTypeEnum] = Field(
        None,
        description="The type of goal, if the category has a goal (TB='Target Category Balance', TBD='Target Category Balance by Date', MF='Monthly Funding', NEED='Plan Your Spending')",
    )


class Category(BaseModel):
    id: UUID
    category_group_id: UUID
    name: str
    hidden: bool = Field(..., description="Whether or not the category is hidden")
    original_category_group_id: Optional[UUID] = Field(
        None,
        description="If category is hidden this is the id of the category group it originally belonged to before it was hidden.",
    )
    note: Optional[str] = None
    budgeted: int = Field(..., description="Budgeted amount in milliunits format")
    activity: int = Field(..., description="Activity amount in milliunits format")
    balance: int = Field(..., description="Balance in milliunits format")
    goal_type: Optional[GoalType] = Field(
        None,
        description="The type of goal, if the category has a goal (TB='Target Category Balance', TBD='Target Category Balance by Date', MF='Monthly Funding', NEED='Plan Your Spending')",
    )
    goal_creation_month: Optional[date] = Field(None, description="The month a goal was created")
    goal_target: Optional[int] = Field(None, description="The goal target amount in milliunits")
    goal_target_month: Optional[date] = Field(
        None,
        description="The original target month for the goal to be completed.  Only some goal types specify this date.",
    )
    goal_percentage_complete: Optional[int] = Field(None, description="The percentage completion of the goal")
    goal_months_to_budget: Optional[int] = Field(
        None,
        description="The number of months, including the current month, left in the current goal period.",
    )
    goal_under_funded: Optional[int] = Field(
        None,
        description="The amount of funding still needed in the current month to stay on track towards completing the goal within the current goal period.  This amount will generally correspond to the 'Underfunded' amount in the web and mobile clients except when viewing a category with a Needed for Spending Goal in a future month.  The web and mobile clients will ignore any funding from a prior goal period when viewing category with a Needed for Spending Goal in a future month.",
    )
    goal_overall_funded: Optional[int] = Field(
        None,
        description="The total amount funded towards the goal within the current goal period.",
    )
    goal_overall_left: Optional[int] = Field(
        None,
        description="The amount of funding still needed to complete the goal within the current goal period.",
    )
    deleted: bool = Field(
        ...,
        description="Whether or not the category has been deleted.  Deleted categories will only be included in delta requests.",
    )


class Data8(BaseModel):
    category: Category
    server_knowledge: int = Field(..., description="The knowledge of the server")


class SaveCategoryResponse(BaseModel):
    data: Data8


class Payee(BaseModel):
    id: UUID
    name: str
    transfer_account_id: Optional[str] = Field(
        None,
        description="If a transfer payee, the `account_id` to which this payee transfers to",
    )
    deleted: bool = Field(
        ...,
        description="Whether or not the payee has been deleted.  Deleted payees will only be included in delta requests.",
    )


class PayeeLocation(BaseModel):
    id: UUID
    payee_id: UUID
    latitude: str
    longitude: str
    deleted: bool = Field(
        ...,
        description="Whether or not the payee location has been deleted.  Deleted payee locations will only be included in delta requests.",
    )


class Cleared(Enum):
    cleared = "cleared"
    uncleared = "uncleared"
    reconciled = "reconciled"


class FlagColorEnum(Enum):
    red = "red"
    orange = "orange"
    yellow = "yellow"
    green = "green"
    blue = "blue"
    purple = "purple"


class FlagColor(BaseModel):
    __root__: Optional[FlagColorEnum] = Field(None, description="The transaction flag")


class SaveSubTransaction(BaseModel):
    amount: int = Field(..., description="The subtransaction amount in milliunits format.")
    payee_id: Optional[UUID] = Field(None, description="The payee for the subtransaction.")
    payee_name: Optional[constr(max_length=50)] = Field(
        None,
        description="The payee name.  If a `payee_name` value is provided and `payee_id` has a null value, the `payee_name` value will be used to resolve the payee by either (1) a matching payee rename rule (only if import_id is also specified on parent transaction) or (2) a payee with the same name or (3) creation of a new payee.",
    )
    category_id: Optional[UUID] = Field(
        None,
        description="The category for the subtransaction.  Credit Card Payment categories are not permitted and will be ignored if supplied.",
    )
    memo: Optional[constr(max_length=200)] = None


class Cleared1(Enum):
    cleared = "cleared"
    uncleared = "uncleared"
    reconciled = "reconciled"


class FlagColor1Enum(Enum):
    red = "red"
    orange = "orange"
    yellow = "yellow"
    green = "green"
    blue = "blue"
    purple = "purple"


class FlagColor1(BaseModel):
    __root__: Optional[FlagColor1Enum] = Field(None, description="The transaction flag")


class TransactionSummary(BaseModel):
    id: str
    date: date = Field(..., description="The transaction date in ISO format (e.g. 2016-12-01)")
    amount: int = Field(..., description="The transaction amount in milliunits format")
    memo: Optional[str] = None
    cleared: Cleared1 = Field(..., description="The cleared status of the transaction")
    approved: bool = Field(..., description="Whether or not the transaction is approved")
    flag_color: Optional[FlagColor1] = Field(None, description="The transaction flag")
    account_id: UUID
    payee_id: Optional[UUID] = None
    category_id: Optional[UUID] = None
    transfer_account_id: Optional[UUID] = Field(
        None, description="If a transfer transaction, the account to which it transfers"
    )
    transfer_transaction_id: Optional[str] = Field(
        None,
        description="If a transfer transaction, the id of transaction on the other side of the transfer",
    )
    matched_transaction_id: Optional[str] = Field(
        None, description="If transaction is matched, the id of the matched transaction"
    )
    import_id: Optional[str] = Field(
        None,
        description="If the Transaction was imported, this field is a unique (by account) import identifier.  If this transaction was imported through File Based Import or Direct Import and not through the API, the import_id will have the format: 'YNAB:[milliunit_amount]:[iso_date]:[occurrence]'.  For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of 'YNAB:-294230:2015-12-30:1'.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be 'YNAB:-294230:2015-12-30:2'.",
    )
    deleted: bool = Field(
        ...,
        description="Whether or not the transaction has been deleted.  Deleted transactions will only be included in delta requests.",
    )


class Type2(Enum):
    transaction = "transaction"
    subtransaction = "subtransaction"


class HybridTransaction(TransactionSummary):
    type: Type2 = Field(
        ...,
        description="Whether the hybrid transaction represents a regular transaction or a subtransaction",
    )
    parent_transaction_id: Optional[str] = Field(
        None,
        description="For subtransaction types, this is the id of the parent transaction.  For transaction types, this id will be always be null.",
    )
    account_name: str
    payee_name: Optional[str] = None
    category_name: Optional[str] = None


class SaveMonthCategory(BaseModel):
    budgeted: int = Field(..., description="Budgeted amount in milliunits format")


class Data17(BaseModel):
    transaction_ids: List[str] = Field(..., description="The list of transaction ids that were imported.")


class TransactionsImportResponse(BaseModel):
    data: Data17


class Bulk(BaseModel):
    transaction_ids: List[str] = Field(..., description="The list of Transaction ids that were created.")
    duplicate_import_ids: List[str] = Field(
        ...,
        description="If any Transactions were not created because they had an `import_id` matching a transaction already on the same account, the specified import_id(s) will be included in this list.",
    )


class Data18(BaseModel):
    bulk: Bulk


class BulkResponse(BaseModel):
    data: Data18


class SubTransaction(BaseModel):
    id: str
    transaction_id: str
    amount: int = Field(..., description="The subtransaction amount in milliunits format")
    memo: Optional[str] = None
    payee_id: Optional[UUID] = None
    payee_name: Optional[str] = None
    category_id: Optional[UUID] = None
    category_name: Optional[str] = None
    transfer_account_id: Optional[UUID] = Field(
        None,
        description="If a transfer, the account_id which the subtransaction transfers to",
    )
    transfer_transaction_id: Optional[str] = Field(
        None,
        description="If a transfer, the id of transaction on the other side of the transfer",
    )
    deleted: bool = Field(
        ...,
        description="Whether or not the subtransaction has been deleted.  Deleted subtransactions will only be included in delta requests.",
    )


class Frequency(Enum):
    never = "never"
    daily = "daily"
    weekly = "weekly"
    everyOtherWeek = "everyOtherWeek"
    twiceAMonth = "twiceAMonth"
    every4Weeks = "every4Weeks"
    monthly = "monthly"
    everyOtherMonth = "everyOtherMonth"
    every3Months = "every3Months"
    every4Months = "every4Months"
    twiceAYear = "twiceAYear"
    yearly = "yearly"
    everyOtherYear = "everyOtherYear"


class FlagColor2Enum(Enum):
    red = "red"
    orange = "orange"
    yellow = "yellow"
    green = "green"
    blue = "blue"
    purple = "purple"


class FlagColor2(BaseModel):
    __root__: Optional[FlagColor2Enum] = Field(None, description="The scheduled transaction flag")


class ScheduledTransactionSummary(BaseModel):
    id: UUID
    date_first: date = Field(
        ...,
        description="The first date for which the Scheduled Transaction was scheduled.",
    )
    date_next: date = Field(
        ...,
        description="The next date for which the Scheduled Transaction is scheduled.",
    )
    frequency: Frequency
    amount: int = Field(..., description="The scheduled transaction amount in milliunits format")
    memo: Optional[str] = None
    flag_color: Optional[FlagColor2] = Field(None, description="The scheduled transaction flag")
    account_id: UUID
    payee_id: Optional[UUID] = None
    category_id: Optional[UUID] = None
    transfer_account_id: Optional[UUID] = Field(
        None,
        description="If a transfer, the account_id which the scheduled transaction transfers to",
    )
    deleted: bool = Field(
        ...,
        description="Whether or not the scheduled transaction has been deleted.  Deleted scheduled transactions will only be included in delta requests.",
    )


class ScheduledSubTransaction(BaseModel):
    id: UUID
    scheduled_transaction_id: UUID
    amount: int = Field(..., description="The scheduled subtransaction amount in milliunits format")
    memo: Optional[str] = None
    payee_id: Optional[UUID] = None
    category_id: Optional[UUID] = None
    transfer_account_id: Optional[UUID] = Field(
        None,
        description="If a transfer, the account_id which the scheduled subtransaction transfers to",
    )
    deleted: bool = Field(
        ...,
        description="Whether or not the scheduled subtransaction has been deleted.  Deleted scheduled subtransactions will only be included in delta requests.",
    )


class MonthSummary(BaseModel):
    month: date
    note: Optional[str] = None
    income: int = Field(
        ...,
        description="The total amount of transactions categorized to 'Inflow: Ready to Assign' in the month",
    )
    budgeted: int = Field(..., description="The total amount budgeted in the month")
    activity: int = Field(
        ...,
        description="The total amount of transactions in the month, excluding those categorized to 'Inflow: Ready to Assign'",
    )
    to_be_budgeted: int = Field(..., description="The available amount for 'Ready to Assign'")
    age_of_money: Optional[int] = Field(None, description="The Age of Money as of the month")
    deleted: bool = Field(
        ...,
        description="Whether or not the month has been deleted.  Deleted months will only be included in delta requests.",
    )


class MonthDetail(MonthSummary):
    categories: List[Category] = Field(
        ...,
        description="The budget month categories.  Amounts (budgeted, activity, balance, etc.) are specific to the {month} parameter specified.",
    )


class ErrorResponse(BaseModel):
    error: ErrorDetail


class Data(BaseModel):
    user: User


class UserResponse(BaseModel):
    data: Data


class BudgetSummary(BaseModel):
    id: UUID
    name: str
    last_modified_on: Optional[datetime] = Field(
        None,
        description="The last time any changes were made to the budget from either a web or mobile client",
    )
    first_month: Optional[date] = Field(None, description="The earliest budget month")
    last_month: Optional[date] = Field(None, description="The latest budget month")
    date_format: Optional[DateFormat] = None
    currency_format: Optional[CurrencyFormat] = None
    accounts: Optional[List[Account]] = Field(
        None,
        description="The budget accounts (only included if `include_accounts=true` specified as query parameter)",
    )


class BudgetDetail(BudgetSummary):
    accounts: Optional[List[Account]] = None
    payees: Optional[List[Payee]] = None
    payee_locations: Optional[List[PayeeLocation]] = None
    category_groups: Optional[List[CategoryGroup]] = None
    categories: Optional[List[Category]] = None
    months: Optional[List[MonthDetail]] = None
    transactions: Optional[List[TransactionSummary]] = None
    subtransactions: Optional[List[SubTransaction]] = None
    scheduled_transactions: Optional[List[ScheduledTransactionSummary]] = None
    scheduled_subtransactions: Optional[List[ScheduledSubTransaction]] = None


class Data3(BaseModel):
    settings: BudgetSettings


class BudgetSettingsResponse(BaseModel):
    data: Data3


class Data4(BaseModel):
    accounts: List[Account]
    server_knowledge: int = Field(..., description="The knowledge of the server")


class AccountsResponse(BaseModel):
    data: Data4


class Data5(BaseModel):
    account: Account


class AccountResponse(BaseModel):
    data: Data5


class SaveAccountWrapper(BaseModel):
    account: SaveAccount


class Data7(BaseModel):
    category: Category


class CategoryResponse(BaseModel):
    data: Data7


class CategoryGroupWithCategories(CategoryGroup):
    categories: List[Category] = Field(
        ...,
        description="Category group categories.  Amounts (budgeted, activity, balance, etc.) are specific to the current budget month (UTC).",
    )


class Data9(BaseModel):
    payees: List[Payee]
    server_knowledge: int = Field(..., description="The knowledge of the server")


class PayeesResponse(BaseModel):
    data: Data9


class Data10(BaseModel):
    payee: Payee


class PayeeResponse(BaseModel):
    data: Data10


class Data11(BaseModel):
    payee_locations: List[PayeeLocation]


class PayeeLocationsResponse(BaseModel):
    data: Data11


class Data12(BaseModel):
    payee_location: PayeeLocation


class PayeeLocationResponse(BaseModel):
    data: Data12


class Data14(BaseModel):
    transactions: List[HybridTransaction]


class HybridTransactionsResponse(BaseModel):
    data: Data14


class SaveTransaction(BaseModel):
    account_id: UUID
    date: date = Field(
        ...,
        description="The transaction date in ISO format (e.g. 2016-12-01).  Future dates (scheduled transactions) are not permitted.  Split transaction dates cannot be changed and if a different date is supplied it will be ignored.",
    )
    amount: int = Field(
        ...,
        description="The transaction amount in milliunits format.  Split transaction amounts cannot be changed and if a different amount is supplied it will be ignored.",
    )
    payee_id: Optional[UUID] = Field(
        None,
        description="The payee for the transaction.  To create a transfer between two accounts, use the account transfer payee pointing to the target account.  Account transfer payees are specified as `tranfer_payee_id` on the account resource.",
    )
    payee_name: Optional[constr(max_length=50)] = Field(
        None,
        description="The payee name.  If a `payee_name` value is provided and `payee_id` has a null value, the `payee_name` value will be used to resolve the payee by either (1) a matching payee rename rule (only if `import_id` is also specified) or (2) a payee with the same name or (3) creation of a new payee.",
    )
    category_id: Optional[UUID] = Field(
        None,
        description="The category for the transaction.  To configure a split transaction, you can specify null for `category_id` and provide a `subtransactions` array as part of the transaction object.  If an existing transaction is a split, the `category_id` cannot be changed.  Credit Card Payment categories are not permitted and will be ignored if supplied.",
    )
    memo: Optional[constr(max_length=200)] = None
    cleared: Optional[Cleared] = Field(None, description="The cleared status of the transaction")
    approved: Optional[bool] = Field(
        None,
        description="Whether or not the transaction is approved.  If not supplied, transaction will be unapproved by default.",
    )
    flag_color: Optional[FlagColor] = Field(None, description="The transaction flag")
    import_id: Optional[constr(max_length=36)] = Field(
        None,
        description="If specified, the new transaction will be assigned this `import_id` and considered \"imported\".  We will also attempt to match this imported transaction to an existing \"user-entered\" transation on the same account, with the same amount, and with a date +/-10 days from the imported transaction date.<br><br>Transactions imported through File Based Import or Direct Import (not through the API) are assigned an import_id in the format: 'YNAB:[milliunit_amount]:[iso_date]:[occurrence]'. For example, a transaction dated 2015-12-30 in the amount of -$294.23 USD would have an import_id of 'YNAB:-294230:2015-12-30:1'.  If a second transaction on the same account was imported and had the same date and same amount, its import_id would be 'YNAB:-294230:2015-12-30:2'.  Using a consistent format will prevent duplicates through Direct Import and File Based Import.<br><br>If import_id is omitted or specified as null, the transaction will be treated as a \"user-entered\" transaction. As such, it will be eligible to be matched against transactions later being imported (via DI, FBI, or API).",
    )
    subtransactions: Optional[List[SaveSubTransaction]] = Field(
        None,
        description="An array of subtransactions to configure a transaction as a split.  Updating `subtransactions` on an existing split transaction is not supported.",
    )


class TransactionDetail(TransactionSummary):
    account_name: str
    payee_name: Optional[str] = None
    category_name: Optional[str] = None
    subtransactions: List[SubTransaction] = Field(..., description="If a split transaction, the subtransactions.")


class SaveMonthCategoryWrapper(BaseModel):
    category: SaveMonthCategory


class BulkTransactions(BaseModel):
    transactions: List[SaveTransaction]


class ScheduledTransactionDetail(ScheduledTransactionSummary):
    account_name: str
    payee_name: Optional[str] = None
    category_name: Optional[str] = None
    subtransactions: List[ScheduledSubTransaction] = Field(
        ..., description="If a split scheduled transaction, the subtransactions."
    )


class Data21(BaseModel):
    months: List[MonthSummary]
    server_knowledge: int = Field(..., description="The knowledge of the server")


class MonthSummariesResponse(BaseModel):
    data: Data21


class Data22(BaseModel):
    month: MonthDetail


class MonthDetailResponse(BaseModel):
    data: Data22


class Data1(BaseModel):
    budgets: List[BudgetSummary]
    default_budget: Optional[BudgetSummary] = Field(
        None,
        description="The default budget, if the associated application is configured to support specifying it",
    )


class BudgetSummaryResponse(BaseModel):
    data: Data1


class Data2(BaseModel):
    budget: BudgetDetail
    server_knowledge: int = Field(..., description="The knowledge of the server")


class BudgetDetailResponse(BaseModel):
    data: Data2


class Data6(BaseModel):
    category_groups: List[CategoryGroupWithCategories]
    server_knowledge: int = Field(..., description="The knowledge of the server")


class CategoriesResponse(BaseModel):
    data: Data6


class Data13(BaseModel):
    transactions: List[TransactionDetail]
    server_knowledge: int = Field(..., description="The knowledge of the server")


class TransactionsResponse(BaseModel):
    data: Data13


class SaveTransactionWrapper(BaseModel):
    transaction: SaveTransaction


class SaveTransactionsWrapper(BaseModel):
    transaction: Optional[SaveTransaction] = None
    transactions: Optional[List[SaveTransaction]] = None


class UpdateTransaction(SaveTransaction):
    id: str


class Data15(BaseModel):
    transaction_ids: List[str] = Field(..., description="The transaction ids that were saved")
    transaction: Optional[TransactionDetail] = Field(
        None,
        description="If a single transaction was specified, the transaction that was saved",
    )
    transactions: Optional[List[TransactionDetail]] = Field(
        None,
        description="If multiple transactions were specified, the transactions that were saved",
    )
    duplicate_import_ids: Optional[List[str]] = Field(
        None,
        description="If multiple transactions were specified, a list of import_ids that were not created because of an existing `import_id` found on the same account",
    )
    server_knowledge: int = Field(..., description="The knowledge of the server")


class SaveTransactionsResponse(BaseModel):
    data: Data15


class Data16(BaseModel):
    transaction: TransactionDetail


class TransactionResponse(BaseModel):
    data: Data16


class Data19(BaseModel):
    scheduled_transactions: List[ScheduledTransactionDetail]
    server_knowledge: int = Field(..., description="The knowledge of the server")


class ScheduledTransactionsResponse(BaseModel):
    data: Data19


class Data20(BaseModel):
    scheduled_transaction: ScheduledTransactionDetail


class ScheduledTransactionResponse(BaseModel):
    data: Data20


class UpdateTransactionsWrapper(BaseModel):
    transactions: List[UpdateTransaction]
