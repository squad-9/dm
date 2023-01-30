find row of max col value:
    df[df.Age == df.Age.max()]
fill na values:
    df.fillna(<value>)
fill na for specific col:
    df[<colname>].fillna(<value>)
remove all rows containing na:
    df.dropna()
remove rows with na in a specific col:
    df.dropna(subset=['<colname>'..],axis=0,inplace=True]
remove cols with na:
    df.dropna([<specific cols if any>],axis=1,inplace=True)
