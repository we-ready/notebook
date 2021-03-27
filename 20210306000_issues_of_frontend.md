---
id: 20210306000_issues_of_frontend
title: 前端开发中的疑难杂症
subtitle: 前端开发中的掉坑和出坑记录
subject: Issues
category: 疑难杂症
tags: form;react-hook-form
keywords: bug;issue
level: 200
cover: https://media.inkscape.org/media/resources/file/Ladybug-icon.png
author: Chris Wei
created_when: 2021-03-06
updated_when: 2021-03-06
---

# 前端开发中的疑难杂症

## 表单内任意的 `button` 点击都会触发 `submit`

> 在自定义表单组件的时候，任何情况下，都需要避免使用 `button`

## `react-hook-form` 向自己二次封装的表单传入 onSubmit 的时候，需要二次传递，而不能直接作为 `handleSubmit` 的参数

> 正确的方式

```
export default function LoginForm ({toLogin}) {

  ...

  const onSubmit = (values) => {
    if (!!toLogin) toLogin(values)
  }
  return (
    <FormContainer>
      <form onSubmit={handleSubmit(onSubmit)}>
  
  ...

```

> 错误的方式

```
export default function LoginForm ({toLogin}) {

  ...

  return (
    <FormContainer>
      <form onSubmit={handleSubmit(toLogin)}>
  
  ...
```

## `react-hook-form` 中使用自定义的 `Input`，每次输入，第一次输入引发的渲染，会终止

#### 自制组件

```
export const MoneyInputField: React.FC<InputFieldProps>  = ({register, variant, type, label, name, placeholder, hint, errors, ...restProps}) => {
  const refSpan = useRef(null);
  const [spanWidth, setSpanWidth] = useState(null)
  const [input, setInput] = useState<string>('');
  
  const onChange = (e) => { 
    setInput(e.target.value) 
  }

  useEffect(() => {
    setSpanWidth(calculateWidth(refSpan?.current))
  }, [refSpan?.current, input]);

  return (
    <InputFieldContainer {...restProps} >
      <InputContainer className={variant} validInput={!!input} >
        <SpanHelper ref={refSpan}>{input || placeholder}</SpanHelper>
        {!input ? null : <InputPrefix>$</InputPrefix> }
        <InputStyled className={variant} type={ type || 'text' } name={name} placeholder= {placeholder} 
          ref={register}
          value={input}
          width={spanWidth || 'auto'}
          onChange={onChange}
        />
      </InputContainer>
    </InputFieldContainer>
  )
}

```

> 因为需要动态调整 `input` 的宽度，所以需要动态获取 `input` 的内容变化，导致这个组件，既像一个受控组件，也像一个非受控组件。

#### 表单

```
export default function PaymentAmountPage ({location}) { 
  const schema = yup.object().shape(SCHEMA);
  const { register, control, handleSubmit, errors, formState: { isDirty } } = useForm({
    // defaultValues: { ...initValues },
    mode: 'onBlur',
    resolver: yupResolver(schema),
  });
  const [amountToPay, setAmountToPay] = useState<number>(0);

  const history = useHistory();
  const data = location?.state?.context;

  const onPay = () => { ... }
  // console.log(data);
  return (
    <>
      <BillContainer>
        <form style={{width: '100%'}} noValidate onSubmit={handleSubmit(onPay)} >
          <MoneyInputField style={{padding: '0 24px'}}
            register={register}
            errors={errors}
            name='amount'
            placeholder='Enter Total Bill Amount Here'
          />
          { !data?.showExcluded ? null :
            <MoneyInputField style={{marginTop: '24px', padding: '0 24px'}} variant="red"
              register={register}
              errors={errors}
              name='excluded'
              placeholder='Enter Excluded Amount Here'
            />
          }

          <SummaryBill onChange={setAmountToPay} control={control} {...data} />

          <div style={{marginTop: '32px', padding:'0 24px'}} >
            <SubmitButton disabled={!isDirty}>Pay Now</SubmitButton>
          </div>
        </form>
      </BillContainer>

```

> 这个案例中，按照非受控组件来使用 `<MoneyInputField>`。

> 同时又要实时根据非受控组件的取值来更新一些内容，因此，引入了 `<SummaryBill>`，去监听表单字段的变化。

> 注意这里的 `<SummaryBill onChange={setAmountToPay} ...`，会引发 `Bug`。

#### 监听实时变化

```
const SummaryBill:React.FC<SummaryBillProps> = ({onChange, control, promotion}) => {
  
  ...

  const values = useWatch<any>({
    control,
    defaultValue: {}
  });

  ...

  const amountToPay     = validBillAmount - discountAmount - voucherDeduction;

  ...

  useEffect(() => {
    if (!!onChange) {
      console.log('onChange amountToPay: ', amountToPay);
      onChange(amountToPay);
    }
  }, [values])

```

#### Bug 描述

当 `SummaryBill` 监听 `values`，并在 `values` 变化之后，把计算结果，通过 `onChange` 回调，回传给 `Form` 组件，而 `Form` 组件又调用 `setAmountToPay` 的时候，`Bug` 出现了。
Bug 的具体表现是：在 `input` 中的输入（键盘），能被代码识别，但无法完成渲染。比如键盘输入：`11`，第一个 `1`，无法渲染到界面。
如果，仅仅停止调用 `setAmountToPay` ， 一切又正常了。
